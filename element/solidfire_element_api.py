import json
import logging
import logging.config
import os

import warnings
import requests
from requests.packages.urllib3 import exceptions

logging.config.fileConfig(os.path.join(os.path.dirname(__file__), "../logging.cfg"))
LOG = logging.getLogger("solidfire_element_api")


class SolidFireRequestException(Exception):
    message = "An unknown exception occurred."

    def __init__(self, arg):
        self.msg = arg


class SolidFireAPI(object):
    """The API for controlling a SolidFire cluster."""
    def __init__(self, *args, **kwargs):
        self.endpoint_dict = kwargs.get('endpoint_dict')
        self.raw = True
        self.request_history = []

    def send_request(self, method, params, version='1.0', endpoint=None):
        if params is None:
            params = {}

        # NOTE(jdg): We allow passing in a new endpoint to issue_api_req
        # to enable some of the multi-cluster features like replication etc
        if endpoint is None:
            endpoint_dict = self.endpoint_dict
        payload = {'method': method, 'params': params}

        url = '%s/json-rpc/%s/' % (endpoint_dict['url'], version)

        LOG.debug('Issue SolidFire API call: %s' % json.dumps(payload))

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", exceptions.InsecureRequestWarning)
            req = requests.post(url,
                                data=json.dumps(payload),
                                auth=(endpoint_dict['login'],
                                      endpoint_dict['password']),
                                verify=False,
                                timeout=30)
        response = req.json()
        req.close()
        # TODO(jdg): Fix the above, failure cases like wrong password
        # missing something that cause req.json to puke

        LOG.debug('Raw response data from SolidFire API: %s' % response)
        # TODO(jdg): Add check/retry catch for things where it's appropriate
        if 'error' in response:
            msg = ('API response: %s'), response
            raise SolidFireRequestException(msg)
        return response['result']

    def clone_volume(self, volume_id, name, new_account_id=None,
                     new_size=None, access=None, snapshot_id=None,
                     attributes=None):
        """CloneVolume is used to create a copy of the volume.

        This method is asynchronous and may take a variable amount of time
        to complete.  The cloning process begins immediately when the
        CloneVolume request is made and is representative of the state of the
        volume when the API method is issued.

        GetAsyncResults can be used to determine when the cloning process is
        complete and the new volume is available for connections.  ListSyncJobs
        can be used to see the progress of creating the clone.

        NOTE: The initial attributes and quality of service settings for
        the volume are inherited from the volume being cloned.  If different
        settings are required, they can be changed via ModifyVolume.

        NOTE: Cloned volumes do not inherit volume access group memberships
        from the source volume."""

        params = {"volumeID": volume_id, "name": name}
        if new_account_id is None:
            params["newAccountID"] = new_account_id
        if new_size is not None:
            params["newSize"] = new_size
        if access is not None:
            params["access"] = access
        if snapshot_id is not None:
            params["snapshotID"] = snapshot_id
        if attributes is not None:
            params["attributes"] = attributes
        return self.send_request('CloneVolume', params)

    def copy_volume(self, volume_id, dst_volume_id, snapshot_id=None):
        """Copies one volume to another."""
        params = {"volumeID": volume_id, "dstVolumeID": dst_volume_id}
        if snapshot_id is not None:
            params["snapshotID"] = snapshot_id
        return self.send_request('CopyVolume', params)

    def cancel_clone(self, clone_id):
        """Cancels a currently running clone operation."""
        params = {"cloneID": clone_id}
        return self.send_request('CancelClone', params)

    def create_volume(self, name, account_id, total_size,
                      enable512e=None, qos=None, attributes=None):
        """CreateVolume is used to create a new (empty) volume on the cluster.

        When the volume is created successfully it is available for connection
        via iSCSI."""

        params = {"name": name,
                  "accountID": account_id,
                  "totalSize": total_size}
        if enable512e is not None:
            params["enable512e"] = enable512e
        if qos is not None:
            params["qos"] = qos
        params['attributes'] = attributes
        return self.send_request('CreateVolume', params)['volumeID']

    def delete_volume(self, volume_id):
        """DeleteVolume marks an active volume for deletion.

        It is purged (permanently deleted) after the cleanup interval elapses.
        After making a request to delete a volume, any active iSCSI connections
        to the volume is immediately terminated and no further connections are
        allowed while the volume is in this state.  It is not returned in
        target discovery requests.

        Any snapshots of a volume that has been marked to delete are not
        affected.  Snapshots are kept until the volume is purged from the
        system.

        If a volume is marked for deletion, and it has a bulk volume read or
        bulk volume write operation in progress, the bulk volume operation is
        stopped.

        If the volume you delete is paired with a volume, replication between
        the paired volumes is suspended and no data is transferred to it or
        from it while in a deleted state.  The remote volume the deleted volume
        was paired with enters into a PausedMisconfigured state and data is no
        longer sent to it or from the deleted volume.  Until the deleted
        volume is purged, it can be restored and data transfers resumes.

        If the deleted volume gets purged from the system, the volume it was
        paired with enters into a StoppedMisconfigured state and the volume
        pairing status is removed.  The purged volume becomes permanently
        unavailable."""

        params = {"volumeID": volume_id}
        return self.send_request('DeleteVolume', params)

    def get_volume_stats(self, volume_id):
        """Retrieves high-level activity measurements for a single volume.

        Values are cumulative from the creation of the volume."""

        params = {"volumeID": volume_id}
        return self.send_request(
            'GetVolumeStats',
            params)

    def list_active_volumes(self, start_volume_id=None, limit=None):
        params = {}
        if start_volume_id is not None:
            params["startVolumeID"] = start_volume_id
        if limit is not None:
            params["limit"] = limit
        return self.send_request(
            'ListActiveVolumes',
            params)['volumes']

    def list_deleted_volumes(self):
        params = {}
        return self.send_request(
            'ListDeletedVolumes',
            params)['volumes']

    def list_volumes(self, start_volume_id=None, limit=None,
                     volume_status=None, accounts=None, is_paired=None):
        params = {}
        if start_volume_id is not None:
            params["startVolumeID"] = start_volume_id
        if limit is not None:
            params["limit"] = limit
        if volume_status is not None:
            params["volumeStatus"] = volume_status
        if accounts is not None:
            params["accounts"] = accounts
        if is_paired is not None:
            params["isPaired"] = is_paired
        return self.send_request('ListVolumes', params)['volumes']

    def list_volumes_for_account(self, account_id,
                                 start_volume_id=None, limit=None):
        params = {"accountID": account_id}
        if start_volume_id is not None:
            params["startVolumeID"] = start_volume_id
        if limit is not None:
            params["limit"] = limit
        return self.send_request(
            'ListVolumesForAccount',
            params)['volumes']

    def modify_volume(self, volume_id, account_id=None,
                      access=None, set_create_time=None, qos=None,
                      total_size=None, attributes=None):
        """ModifyVolume is used to modify settings on an existing volume.

        Modifications can be made to one volume at a time and changes take
        place immediately.  If an optional parameter is left unspecified,
        the value will not be changed.

        Extending the size of a volume that is being replicated should be done
        in an order.  The target (Replication Target) volume should first be
        increased in size, then the source (Read/Write) volume can be resized.
        It is recommended that both the target and the source volumes be the
        same size.

        NOTE: If you change access status to locked or target all existing
        iSCSI connections are terminated."""

        params = {"volumeID": volume_id}
        if account_id is not None:
            params["accountID"] = account_id
        if access is not None:
            params["access"] = access
        if set_create_time is not None:
            params["setCreateTime"] = set_create_time
        if qos is not None:
            params["qos"] = qos
        if total_size is not None:
            params["totalSize"] = total_size
        if attributes is not None:
            params["attributes"] = attributes
        return self.send_request('ModifyVolume', params)

    def purge_deleted_volume(self, volume_id):
        """PurgeDeletedVolume immediately and permanently purges a volume.

        A volume must be deleted using DeleteVolume before it can be purged.
        Volumes are purged automatically after a period of time, so usage of
        this method is not typically required."""

        params = {"volumeID": volume_id}
        return self.send_request(
            'PurgeDeletedVolume',
            params)

    def add_account(self, username, initiator_secret=None,
                    target_secret=None, attributes=None):
        """AddAccount is used to add a new account to the system.

        New volumes can be created under the new account.
        The CHAP settings specified for the account applies to all volumes
        owned by the account."""

        params = {"username": username}
        if initiator_secret is not None:
            params["initiatorSecret"] = initiator_secret
        if target_secret is not None:
            params["targetSecret"] = target_secret
        if attributes is not None:
            params["attributes"] = attributes
        return self.send_request('AddAccount', params)

    def get_account_by_id(self, account_id):
        """Get account information, given the ID."""
        params = {"accountID": account_id}
        return self.send_request('GetAccountByID', params)

    def get_account_by_name(self, username):
        """Get account information, given the ID."""
        params = {"username": username}
        return self.send_request('GetAccountByName', params)

    def get_account_efficiency(self, account_id):
        return self.send_request('GetAccountEfficiency', {})

    def list_accounts(self, start_account_id=None, limit=None):
        """Returns list of accounts, with optional paging support."""
        params = {}
        if start_account_id is not None:
            params["startAccountID"] = start_account_id
        if limit is not None:
            params["limit"] = limit
        return self.send_request('ListAccounts', params)['accounts']

    def modify_account(self, account_id, status=None,
                       initiator_secret=None, target_secret=None,
                       attributes=None):
        params = {}
        params['accountID'] = account_id
        if status:
            if status in ['active', 'locked']:
                params['status'] = status
            else:
                raise
        if initiator_secret:
            params['initiator_secret'] = initiator_secret
        if target_secret:
            params['target_secret'] = target_secret
        if attributes:
            params['attributes'] = attributes
        return self.send_request('ModifyAccount', params)

    def remove_account(self, account_id):
        """Remove an account from the system.

        All Volumes must be deleted and purged on the account before it can
        be removed.  If volumes on the account are still pending deletion, use
        PurgeVolume purge deleted volumes."""

        params = {"accountID": account_id}
        return self.send_request('RemoveAccount', params)

    # ### Cluster admin operations  ####
    def get_cluster_capacity(self):
        """Return the high-level capacity measurements for an entire cluster.

        The fields returned from this method can be used to calculate the
        efficiency rates that are displayed in the Element User Interface."""

        params = {}
        return self.send_request(
            'GetClusterCapacity',
            params)

    def get_cluster_info(self):
        """Return configuration information about the cluster."""
        params = {}
        return self.send_request(
            'GetClusterInfo',
            params)

    def get_cluster_version_info(self):
        """Return Element software version info for each node in the cluster.

        Information about the nodes that are currently in the process of
        upgrading software is also returned."""
        params = {}
        return self.send_request(
            'GetClusterVersionInfo',
            params)

    def get_limits(self):
        """Retrieves the limit values set by the API"""
        params = {}
        return self.send_request('GetLimits', params)

    def list_services(self):
        """List the services in the cluster."""
        params = {}
        return self.send_request('ListServices', params)

    def get_async_result(self, async_handle):
        """Used to retrieve the result of asynchronous method calls.

        Some method calls are long running and do not complete when the initial
        response is sent.  To obtain the result of the method call, polling
        with GetAsyncResult is required.

        GetAsyncResult returns the overall status of the operation
        (in progress, completed, or error) in a standard fashion,but the actual
        data returned for the operation depends on the original method call
        and the return data is documented with each method.

        The result for a completed asynchronous method call can only be
        retrieved once.  Once the final result has been returned, later
        attempts returns an error."""

        params = {"asyncHandle": async_handle}
        return self.send_request(
            'GetAsyncResult',
            params)

    def create_snapshot(self, volume_id, snapshot_id=None,
                        name=None, attributes=None):
        """CreateSnapshot is used to create a point-in-time copy of a volume.

        A snapshot can be created from any volume or from an existing snapshot.

        NOTE: Creating a snapshot is allowed if cluster fullness is at stage
        2 or 3.  Snapshots are not created when cluster fullness is at
        stage 4 or 5."""

        params = {"volumeID": volume_id}
        if snapshot_id is not None:
            params["snapshotID"] = snapshot_id
        if name is not None:
            params["name"] = name
        if attributes is not None:
            params["attributes"] = attributes
        return self.send_request(
            'CreateSnapshot',
            params)

    def delete_snapshot(self, snapshot_id):
        """DeleteSnapshot is used to delete a snapshot.

        A snapshot that is currently the "active" snapshot cannot be deleted.
        You must rollback and make another snapshot "active" before the current
        snapshot can be deleted.  To rollback a snapshot,
        use RollbackToSnapshot."""

        params = {"snapshotID": snapshot_id}
        return self.send_request(
            'DeleteSnapshot',
            params)

    def list_snapshots(self, volume_id=None):
        """Used to return attributes of each snapshot taken on the volume."""

        params = {}
        if volume_id is not None:
            params["volumeID"] = volume_id
        return self.send_request('ListSnapshots', params)['snapshots']

    def list_active_nodes(self):
        params = {}
        return self.send_request(
            'ListActiveNodes',
            params)

    def list_all_nodes(self):
        params = {}
        return self.send_request('ListAllNodes', params)

    def list_pending_nodes(self):
        """Gets the list of pending nodes.

        Pending nodes are running and configured to join the cluster,
        but have not been added via the AddNodes method."""

        params = {}
        return self.send_request(
            'ListPendingNodes',
            params)

    def create_volume_access_group(self, name, initiators=None,
                                   volumes=None, attributes=None):
        """Creates a new volume access group.

        The new volume access group must be given a name when it is created.
        Entering initiators and volumes are optional when creating a volume
        access group.  Once the group is created volumes and initiator IQNs
        can be added.  Any initiator IQN that is successfully added to the
        volume access group is able to access any volume in the group without
        CHAP authentication."""

        params = {"name": name}
        if initiators is not None:
            params["initiators"] = initiators
        if volumes is not None:
            params["volumes"] = volumes
        if attributes is not None:
            params["attributes"] = attributes
        return self.send_request(
            'CreateVolumeAccessGroup',
            params)

    def list_volume_access_groups(self,
                                  start_volume_access_group_id=None,
                                  limit=None):
        """"""
        params = {}
        if start_volume_access_group_id is not None:
            params["startVolumeAccessGroupID"] = start_volume_access_group_id
        if limit is not None:
            params["limit"] = limit
        return self.send_request(
            'ListVolumeAccessGroups',
            params)

    def delete_volume_access_group(self, volume_access_group_id):
        """Delete a volume access group from the system."""
        params = {"volumeAccessGroupID": volume_access_group_id}
        return self.send_request(
            'DeleteVolumeAccessGroup',
            params)

    def modify_volume_access_group(self, volume_access_group_id,
                                   name=None, initiators=None,
                                   volumes=None, attributes=None):
        """Update initiators and add/remove volumes from a volume access group.

        A specified initiator or volume that duplicates an existing volume
        or initiator in a volume access group is left as-is. If a value is not
        specified for volumes or initiators, the current list of initiators
        and volumes are not changed.

        Often, it is easier to use the convenience functions to modify
        initiators and volumes independently:

         - AddInitiatorsToVolumeAccessGroup
         - RemoveInitiatorsFromVolumeAccessGroup
         - AddVolumesToVolumeAccessGroup
         - RemoveVolumesFromVolumeAccessGroup"""

        params = {"volumeAccessGroupID": volume_access_group_id}
        if name is not None:
            params["name"] = name
        if initiators is not None:
            params["initiators"] = initiators
        if volumes is not None:
            params["volumes"] = volumes
        if attributes is not None:
            params["attributes"] = attributes
        return self.send_request(
            'ModifyVolumeAccessGroup',
            params)

    def add_initiators_to_volume_access_group(self,
                                              volume_access_group_id,
                                              initiators):
        """Add initiators to a volume access group."""
        params = {
            "volumeAccessGroupID": volume_access_group_id,
            "initiators": initiators}
        return self.send_request(
            'AddInitiatorsToVolumeAccessGroup',
            params)

    def remove_initiators_from_volume_access_group(self,
                                                   volume_access_group_id,
                                                   initiators):
        """Remove initiators from a volume access group."""
        params = {
            "volumeAccessGroupID": volume_access_group_id,
            "initiators": initiators}
        return self.send_request(
            'RemoveInitiatorsFromVolumeAccessGroup',
            params)

    def add_volumes_to_volume_access_group(
            self,
            volume_access_group_id,
            volumes):
        """Add volumes to a volume access group."""
        params = {
            "volumeAccessGroupID": volume_access_group_id,
            "volumes": volumes}
        return self.send_request(
            'AddVolumesToVolumeAccessGroup',
            params)

    def remove_volumes_from_volume_access_group(
            self,
            volume_access_group_id,
            volumes):
        """Remove volumes from a volume access group."""
        params = {
            "volumeAccessGroupID": volume_access_group_id,
            "volumes": volumes}
        return self.send_request(
            'RemoveVolumesFromVolumeAccessGroup',
            params)

    def create_database_entry(self, path, data=None):
        """Creates a new database entry"""
        params = {"path": path}
        if data is not None:
            params["data"] = data
        return self.send_request(
            'CreateDatabaseEntry',
            params)

    def delete_database_entry(self, path, data_version):
        """Deletes an existing database entry"""
        params = {"path": path, "dataVersion": data_version}
        return self.send_request(
            'DeleteDatabaseEntry',
            params)

    def get_database_entry(self, path):
        """Gets an entry from the database"""
        params = {"path": path}
        return self.send_request(
            'GetDatabaseEntry',
            params)

    def set_database_entry(self, path, data_version, data):
        """Sets the contents of an existing database entry"""
        params = {"path": path, "dataVersion": data_version, "data": data}
        return self.send_request(
            'SetDatabaseEntry',
            params)

    def list_database_children(self, path):
        """Returns a list of the names of the children for a database path"""
        params = {"path": path}
        return self.send_request(
            'ListDatabaseChildren',
            params)

    def list_database_children_data(self, path):
        """Returns the data for all children in a database path"""
        params = {"path": path}
        return self.send_request(
            'ListDatabaseChildrenData',
            params)
