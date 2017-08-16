SolidFire CLI Tools for Storage Clusters
=================================================
This tool is intended to be an easy-to-use command-line interface that enables you to do the following:

1. Quickly install a fully functional interface to the JSON-RPC using pip.
2. Get help on how to use the commands by accessing the inline help.
3. Execute any command supported by NetApp SolidFire Element OS version 9.1.
4. Utilize autofill on MacOS and Linux distributions to make constructing commands easier.
5. Get responses in three different output formats: tree format, JSON format, and pickle format.
6. Execute any non-public commands by using "sfcli sfapi invoke" with the necessary method name and parameters.
7. Achieve the same functionality as the SDKs without ever opening an editor.
8. Establish and store connection information locally.

Audience
-----------------
The tool is for users who do not want to use PowerShell. It integrates as you would expect with bash. The main advantages
of using this tool are the following:
* Objects are returned as strings, which allows for expeditious grepping.
* It is very easy to install and use.

Installing SolidFire CLI Tools
----------
If you are on a mac, you will have to set up a virtual environment first because the native mac python does not support setuptools. To create a virtualenvironment, run

    pip install virtualenv
    virtualenv pythoncli
    source pythoncli/bin/activate # This activates the virtual environment. 

Next, irrespective of your OS there are a few ways you can install the tool: from source or from pypi, using easy_install or using pip.

To install from pypi using pip, execute the following command:

    pip install solidfire-cli

To install from source using easy_install, navigate to solidfirecli*.tar.gz file (where the * stands for the version), and run

	easy_install solidfirecli*.tar.gz

Supported Operating Systems
-----------------------------------
* Windows 7, 8, and 10
* Linux
* MacOS

## Documentation

[User Guide](https://solidfire.github.io/solidfire-cli/NetApp_SolidFire_CLI_User_Guide.pdf) This readme in .pdf form.

[Release Notes](https://solidfire.github.io/solidfire-cli/NetApp_SolidFire_CLI_Release_Notes.pdf) v1.4

Accessing Inline Help
---------------------
The tool includes inline help that provides details about how to use the commands.

To see the top-level help, run:

    sfcli --help

To see the help at the object level (for example, account), run:

    sfcli account --help

To see command-specific help, run:

    sfcli account getbyid --help

Enabling Autocomplete
---------------------
Autocomplete is only available on mac and linux. To enable it, enter the following into your .bashrc file or run it whenever you want autocomplete enabled:

    eval "$(_SFCLI_COMPLETE=source sfcli)"

Managing Connections
---------------------
To run a command on a given connection without storing it away, use the mvip, username, and password options at the top level.

    sfcli --mvip 10.117.60.15 --username username --password password account list

To connect to an individual node rather than the cluster admin node, add `--port 442` to connection options.

To store a given connection, use the connection push command and supply the name option.

    sfcli connection push --mvip 10.117.60.15 --username username --password password --name "Example"

There are three ways to access a stored connection: by name, by index, or by default. To access a connection by name, use -n or --name. To access a connection by index, use -c or --connectionIndex. To access a connection by default, leave the above two parameters off and the command will default to using the connection at index 0. The three possibilities are exemplified below:

    sfcli -n Example account list # by name
    sfcli -c 0 account list # by index
    sfcli account list # use connection 0

To remove a given connection, use the connection remove command.

    sfcli connection remove -n Example
    sfcli connection remove -i -1 # Removes the newly pushed connection.
    sfcli connection remove -i 0 # Removes the oldest pushed connection.
    sfcli connection remove -i 1 # Removes the second oldest connection.

To list the stored connections, use the Connection List command.

	sfcli connection list

To prune broken connections from the connections.csv file, use the Connection Prune command.

	sfcli connection prune

Executing Commands with Standard Parameters
------------------
Determine the needed parameters using the autocomplete functionality or the --help functionality and then append the required parameters at the end as shown below:

    sfcli -c 0 account getbyid --accountid 3065

Example output:

    account:
        attributes:
        target_secret:
            secret:   q7788;0a:Cd0xCE4
        initiator_secret:
            secret:   r0Ju1}t:02"5p<L^
        status:   active
        account_id:   3065
        username:   example
        volumes:

Executing Commands with Grouped Parameters
------------------------------------------
A parameter might have optional subparameters that you need to use to specify an attribute of the the parameter.
In the following example, the --volumes parameter has subparameters, such as volumeid, accessvolumes, name, newaccountid, newsize,and attributes:

    sfcli volume clonemultiple --help

    Usage: sfcli volume clonemultiple [OPTIONS]

      CloneMultipleVolumes enables you to create a clone of a group of specified
      volumes. You can assign a consistent set of characteristics to a group of
      multiple volumes when they are cloned together. Before using groupSnapShotID
      to clone the volumes in a group snapshot, you must create the group snapshot
      by using the CreateGroupSnapShot API method or the Element OS Web UI. Using
      groupSnapshotID is optional when cloning multiple volumes.
      Note: Cloning multiple volumes is allowed if cluster fullness is at stage 2 or 3.
      Clones are not created when cluster fullness is at stage 4 or 5.

    Options:
      --volumes                      Unique ID for each volume to include
                                     in the clone. If optional parameters are not specified,
                                     the values are inherited from the source
                                     volumes.  Has the following subparameters:
                                     --volumeid --accessvolumes --name
                                     --newaccountidvolumes --newsize --attributes
                                     [required]
      --volumeid INTEGER             [subparameter] Required parameter for
                                     "volumes" array: volumeID.  [required]
      --accessvolumes TEXT           [subparameter] Access settings for the new
                                     volume. readOnly: Only read operations are
                                     allowed. readWrite: Reads and writes are
                                     allowed. locked: No reads or writes are
                                     allowed. replicationTarget: Identify a volume
                                     as the target volume for a paired set of
                                     volumes. If the volume is not paired, the
                                     access status is locked.  If unspecified, the
                                     access settings of the clone will be the same
                                     as the source.
      --name TEXT                    [subparameter] New name for the clone.
      --newaccountidvolumes INTEGER  [subparameter] Account ID for the new volume.
      --newsize INTEGER              [subparameter] New size Total size of the
                                     volume, in bytes. Size is rounded up to the
                                     nearest 1MB size.
      --attributes TEXT              [subparameter] List of name-value pairs in
                                     JSON object format.
      --access TEXT                  New default access method for the new volumes
                                     if not overridden by information passed in
                                     the volume's array. readOnly: Only read
                                     operations are allowed. readWrite: Reads and
                                     writes are allowed. locked: No reads or
                                     writes are allowed. replicationTarget:
                                     Identify a volume as the target volume for a
                                     paired set of volumes. If the volume is not
                                     paired, the access status is locked.  If
                                     unspecified, the access settings of the clone
                                     will be the same as the source.
      --groupsnapshotid INTEGER      ID of the group snapshot to use as a basis
                                     for the clone.
      --newaccountid INTEGER         New account ID for the volumes if not
                                     overridden by information passed in the
                                     volumes array.
      --help                         Show this message and exit.

To clone multipe volumes in the same group, run:

    sfcli volume clonemultiple --volumes --volumeid 1 --accessvolumes readWrite --volumes --volumeid 1

This clones the volumes and applies readWrite access to volume 1 and uses the default for volume 2.

Executing Commands with Nonstandard Parameters
------------------------------------------------
Occasionally, you will need to pass in an arbitrary dictionary of keys and values. In that case,
you will need to provide a JSON string directly to the command line.

In the example below, if you want to bypass the logic and make a call directly to the API, you can
do so by using SFApi Invoke.

#### SFApi Invoke ####

    $account = sfcli -c 0 SFApi Invoke --method GetAccountByID --parameters "{\"accountID\":94}"

Output Formats
--------------
#### Tree Format (Default) ####
The tree format enables you to  grep the output and get
a result without extra formatting. It uses whitespace to distinguish between different objects. To
view this format, run a command without the -j or -k options.

See the following example:

    accounts:

            attributes:
            storage_container_id:
                int:   <to see more details, increase depth>
            account_id:   2404
            status:   active
            initiator_secret:
                secret:   <to see more details, increase depth>
            target_secret:
                secret:   <to see more details, increase depth>
            volumes:
                <to see more details, increase depth>
            username:   EXAMPLE

            attributes:
            storage_container_id:
                int:   <to see more details, increase depth>
            account_id:   2405
            status:   active
            initiator_secret:
                secret:   <to see more details, increase depth>
            target_secret:
                secret:   <to see more details, increase depth>
            volumes:
            username:   haxecliFV8QdeT6fn5DxtvFuYzjsFwWtc1YzXfT5-NQE5pHiQAQBelNqVskTsJY8

            attributes:
            storage_container_id:
                int:   <to see more details, increase depth>
            account_id:   2406
            status:   active
            initiator_secret:
                secret:   <to see more details, increase depth>
            target_secret:
                secret:   <to see more details, increase depth>
            volumes:
            username:   haxeclij0yA7YVfCDiq9jZXdkdiKfkSytK2flKk9Gi9NFq0677Fcg44QIDc9inqF

#### JSON Format ####
The output in JSON format resembles the output of the API. This can be useful if you are going
to store the data for later use with Postman or if you want to import it via any JSON libraries.
To get this output, use the -j option after "sfcli" in your command.

See the following example:

    {
        "accounts": [
            {
                "attributes": {},
                "initiator_secret": {
                    "secret": "3,gG[sP02V'@911}"
                },
                "volumes": [
                    4588
                ],
                "target_secret": {
                    "secret": "aAe6Bb&q]63zU0Ei"
                },
                "status": "active",
                "account_id": 2404,
                "username": "EXAMPLE",
                "storage_container_id": {
                    "hex": "00000000000000000000000000000000"
                }
            },
            {
                "attributes": {},
                "initiator_secret": {
                    "secret": "haxecliiSgmB"
                },
                "volumes": [],
                "target_secret": {
                    "secret": "haxecliLUuvO9s"
                },
                "status": "active",
                "account_id": 2405,
                "username": "haxecliFV8QdeT6fn5DxtvFuYzjsFwWtc1YzXfT5-NQE5pHiQAQBelNqVskTsJY8",
                "storage_container_id": {
                    "hex": "00000000000000000000000000000000"
                }
            },
            {
                "attributes": {},
                "initiator_secret": {
                    "secret": "haxecli7tOAtk"
                },
                "volumes": [],
                "target_secret": {
                    "secret": "haxecliXFty4F2"
                },
                "status": "active",
                "account_id": 2406,
                "username": "haxeclij0yA7YVfCDiq9jZXdkdiKfkSytK2flKk9Gi9NFq0677Fcg44QIDc9inqF",
                "storage_container_id": {
                    "hex": "00000000000000000000000000000000"
                }
            }
        ]
    }

#### Pickle Format ####
The pickle format is the same as the JSON format except with an extra field for every object.
This field names the object type. This is useful if you want to store the data and use
it with a Python SDK later. If you unpickle the string using the Python SDK, you get
a full object model instead of a nested dictionary. To get this output, use the -k option after "sfcli" in your command.

See the following example:

    {
        "py/object": "solidfire.models.ListAccountsResult",
        "accounts": [
            {
                "account_id": 2404,
                "attributes": {},
                "status": "active",
                "py/object": "solidfire.models.Account",
                "target_secret": {
                    "secret": "aAe6Bb&q]63zU0Ei",
                    "py/object": "solidfire.custom.models.CHAPSecret"
                },
                "initiator_secret": {
                    "secret": "3,gG[sP02V'@911}",
                    "py/object": "solidfire.custom.models.CHAPSecret"
                },
                "username": "EXAMPLE",
                "volumes": [
                    4588
                ],
                "storage_container_id": {
                    "hex": "00000000000000000000000000000000",
                    "py/object": "uuid.UUID"
                }
            },
            {
                "account_id": 2405,
                "attributes": {},
                "status": "active",
                "py/object": "solidfire.models.Account",
                "target_secret": {
                    "secret": "haxecliLUuvO9s",
                    "py/object": "solidfire.custom.models.CHAPSecret"
                },
                "initiator_secret": {
                    "secret": "haxecliiSgmB",
                    "py/object": "solidfire.custom.models.CHAPSecret"
                },
                "username": "haxecliFV8QdeT6fn5DxtvFuYzjsFwWtc1YzXfT5-NQE5pHiQAQBelNqVskTsJY8",
                "volumes": [],
                "storage_container_id": {
                    "hex": "00000000000000000000000000000000",
                    "py/object": "uuid.UUID"
                }
            },
            {
                "account_id": 2406,
                "attributes": {},
                "status": "active",
                "py/object": "solidfire.models.Account",
                "target_secret": {
                    "secret": "haxecliXFty4F2",
                    "py/object": "solidfire.custom.models.CHAPSecret"
                },
                "initiator_secret": {
                    "secret": "haxecli7tOAtk",
                    "py/object": "solidfire.custom.models.CHAPSecret"
                },
                "username": "haxeclij0yA7YVfCDiq9jZXdkdiKfkSytK2flKk9Gi9NFq0677Fcg44QIDc9inqF",
                "volumes": [],
                "storage_container_id": {
                    "hex": "00000000000000000000000000000000",
                    "py/object": "uuid.UUID"
                }
            }
        ]
    }

Error Logging
-------
You can choose from four different levels of logging:
* 0: Critical logging. Only shows errors.
* 1: Warning logging. Shows errors and warnings.
* 2: Info logging. Shows errors, warnings, and information.
* 3: Debug logging. Shows errors, warning, information, and debug information.

To set the debug level, use the --debug option after "sfcli" in your command. The logger is a standard, Pythonic logger. In bash, the standard way to store information from different streams is to specify the stream you wish to redirect to a folder.

In the following example, when you run:

	sfcli --debug 2 account list

You get the following information printed:

	INFO in cmd_account.py@50: startaccountid = None;limit = None;

And you get the following data:

	accounts:

If you want to store the response from the server, you can run the command as follows:

	sfcli --debug 2 account list > data.txt

If you want to store the information from the server, you can run the command as follows:

	sfcli --debug 2 account list 2> info.txt

In this case, the info.txt file only contains the text labeled "INFO" and the data.txt file only contains the text labeled "accounts:".


Command Options
---------------
You can use the following options in the tool:

    -m, --mvip TEXT
        SolidFire MVIP
    -l, --login TEXT
        SolidFire Cluster login
    -p, --password TEXT
        SolidFire Cluster password
    -q, --port INTEGER
        The port number on which you wish to connect
    -n, --name TEXT
        The name of the connection you wish to use in connections.csv. You can use this if you have previously stored away a connection.
    -c, --connectionIndex INTEGER
        The index of the connection you wish to use in connections.csv. You can use this if you have previously stored away a connection.
    -j, --json
        To print the full output in json format, use this flag
    -k, --pickle
        To print the full output in a pickled json format, use this flag.
    -d, --depth INTEGER
        To print the output as a tree and specify the depth, use this option.
    -f, --filter_tree TEXT
        To filter the fields that will be displayed in a tree, use this parameter. Supply fields in a comma separated list of keypaths. For example, to filter accounts list, if I wanted only the username and status, I could supply 'accounts.username,accounts.status'.
    --debug [0|1|2|3]
        Set the debug level
    --help
        Show this help and exit.

ClusterAdmin Commands 
---------------------------------------------------------------
#### modify ####
Command:

    sfcli ClusterAdmin modify <options>

Description:

You can use ModifyClusterAdmin to change the settings for a cluster admin or LDAP cluster admin. You cannot change access for the administrator cluster admin account. 

Options:
--clusteradminid
ClusterAdminID for the cluster admin or LDAP cluster admin to modify. 

--password
Password used to authenticate this cluster admin. 

--access
Controls which methods this cluster admin can use. For more details, see Access Control in the Element API Reference Guide. 

--attributes
List of name-value pairs in JSON object format. 

---------------------------------------------------------------
#### list ####
Command:

    sfcli ClusterAdmin list <options>

Description:

ListClusterAdmins returns the list of all cluster administrators for the cluster. There can be several cluster administrator accounts with different levels of permissions. There can be only one primary cluster administrator in the system. The primary Cluster Admin is the administrator that was created when the cluster was created. You can also create LDAP administrators when setting up an LDAP system on the cluster. 

Options:
---------------------------------------------------------------
#### getcurrent ####
Command:

    sfcli ClusterAdmin getcurrent <options>

Description:

GetCurrentClusterAdmin returns information for the current primary cluster administrator. The primary Cluster Admin was created when the cluster was created. 

Options:
---------------------------------------------------------------
#### remove ####
Command:

    sfcli ClusterAdmin remove <options>

Description:

You can use RemoveClusterAdmin to remove a Cluster Admin. You cannot remove the administrator cluster admin account. 

Options:
--clusteradminid
ClusterAdminID for the cluster admin to remove. 

---------------------------------------------------------------
#### add ####
Command:

    sfcli ClusterAdmin add <options>

Description:

You can use AddClusterAdmin to add a new cluster admin account. A cluster ddmin can manage the cluster using the API and management tools. Cluster admins are completely separate and unrelated to standard tenant accounts. Each cluster admin can be restricted to a subset of the API. NetApp recommends using multiple cluster admin accounts for different users and applications. You should give each cluster admin the minimal permissions necessary; this reduces the potential impact of credential compromise. You must accept the End User License Agreement (EULA) by setting the acceptEula parameter to true to add a cluster administrator account to the system. 

Options:
--username
Unique username for this cluster admin. Must be between 1 and 1024 characters in length. 

--password
Password used to authenticate this cluster admin. 

--access
Controls which methods this cluster admin can use. For more details on the levels of access, see Access Control in the Element API Reference Guide. 

--accepteula
Required to indicate your acceptance of the End User License Agreement when creating this cluster. To accept the EULA, set this parameter to true. 

--attributes
List of name-value pairs in JSON object format. 


Sensors Commands 
---------------------------------------------------------------
#### getipmiinfo ####
Command:

    sfcli Sensors getipmiinfo <options>

Description:

GetIpmiInfo enables you to display a detailed reporting of sensors (objects) for node fans, intake and exhaust temperatures, and power supplies that are monitored by the system. 

Options:
---------------------------------------------------------------
#### getipmiconfig ####
Command:

    sfcli Sensors getipmiconfig <options>

Description:

GetIpmiConfig enables you to retrieve hardware sensor information from sensors that are in your node. 

Options:
--chassistype
Displays information for each node chassis type. Valid values are: all: Returns sensor information for each chassis type. {chassis type}: Returns sensor information for a specified chassis type. 


StorageContainer Commands 
---------------------------------------------------------------
#### modify ####
Command:

    sfcli StorageContainer modify <options>

Description:

ModifyStorageContainer enables you to make changes to an existing virtual volume storage container. 

Options:
--storagecontainerid
The unique ID of the virtual volume storage container to modify. 

--initiatorsecret
The new secret for CHAP authentication for the initiator. 

--targetsecret
The new secret for CHAP authentication for the target. 

---------------------------------------------------------------
#### list ####
Command:

    sfcli StorageContainer list <options>

Description:

ListStorageContainers enables you to retrieve information about all virtual volume storage containers known to the system. 

Options:
--storagecontainerids
A list of storage container IDs for which to retrieve information. If you omit this parameter, the method returns information about all storage containers in the system. 

---------------------------------------------------------------
#### delete ####
Command:

    sfcli StorageContainer delete <options>

Description:

DeleteStorageContainers enables you to remove up to 2000 Virtual Volume (VVol) storage containers from the system at one time. The storage containers you remove must not contain any VVols. 

Options:
--storagecontainerids
A list of IDs of the storage containers to delete. You can specify up to 2000 IDs in the list. 

---------------------------------------------------------------
#### create ####
Command:

    sfcli StorageContainer create <options>

Description:

CreateStorageContainer enables you to create a Virtual Volume (VVol) storage container. Storage containers are associated with a SolidFire storage system account, and are used for reporting and resource allocation. Storage containers can only be associated with virtual volumes. You need at least one storage container to use the Virtual Volumes feature. 

Options:
--name
The name of the storage container. Follows SolidFire account naming restrictions. 

--initiatorsecret
The secret for CHAP authentication for the initiator. 

--targetsecret
The secret for CHAP authentication for the target. 

--accountid
Non-storage container account that will become a storage container. 

---------------------------------------------------------------
#### getefficiency ####
Command:

    sfcli StorageContainer getefficiency <options>

Description:

GetStorageContainerEfficiency enables you to retrieve efficiency information about a virtual volume storage container. 

Options:
--storagecontainerid
The ID of the storage container for which to retrieve efficiency information. 


SFApi Commands 
---------------------------------------------------------------
#### invoke ####
Command:

    sfcli SFApi invoke <options>

Description:

This will invoke any API method supported by the SolidFire API for the version and port the connection is using. Returns a nested hashtable of key/value pairs that contain the result of the invoked method. 

Options:
--method
The name of the method to invoke. This is case sensitive. 

--parameters
An object, normally a dictionary or hashtable of the key/value pairs, to be passed as the params for the method being invoked. 


VolumeAccessGroup Commands 
---------------------------------------------------------------
#### modify ####
Command:

    sfcli VolumeAccessGroup modify <options>

Description:

You can use ModifyVolumeAccessGroup to update initiators and add or remove volumes from a volume access group. If a specified initiator or volume is a duplicate of what currently exists, the volume access group is left as-is. If you do not specify a value for volumes or initiators, the current list of initiators and volumes is not changed. 

Options:
--volumeaccessgroupid
The ID of the volume access group to modify. 

--virtualnetworkid
The ID of the SolidFire virtual network to associate the volume access group with. 

--virtualnetworktags
The ID of the SolidFire virtual network to associate the volume access group with. 

--name
The new name for this volume access group. Not required to be unique, but recommended. 

--initiators
List of initiators to include in the volume access group. If unspecified, the access group's configured initiators are not modified. 

--volumes
List of volumes to initially include in the volume access group. If unspecified, the access group's volumes are not modified. 

--deleteorphaninitiators
true: Delete initiator objects after they are removed from a volume access group. false: Do not delete initiator objects after they are removed from a volume access group. 

--attributes
List of name-value pairs in JSON object format. 

---------------------------------------------------------------
#### delete ####
Command:

    sfcli VolumeAccessGroup delete <options>

Description:

DeleteVolumeAccessGroup enables you to delete a volume access group. 

Options:
--volumeaccessgroupid
The ID of the volume access group to be deleted. 

---------------------------------------------------------------
#### create ####
Command:

    sfcli VolumeAccessGroup create <options>

Description:

You can use CreateVolumeAccessGroup to create a new volume access group. When you create the volume access group, you need to give it a name, and you can optionally enter initiators and volumes. After you create the group, you can add volumes and initiator IQNs. Any initiator IQN that you add to the volume access group is able to access any volume in the group without CHAP authentication. 

Options:
--name
The name for this volume access group. Not required to be unique, but recommended. 

--initiators
List of initiators to include in the volume access group. If unspecified, the access group's configured initiators are not modified. 

--volumes
List of volumes to initially include in the volume access group. If unspecified, the access group's volumes are not modified. 

--virtualnetworkid
The ID of the SolidFire virtual network to associate the volume access group with. 

--virtualnetworktags
The ID of the SolidFire virtual network to associate the volume access group with. 

--attributes
List of name-value pairs in JSON object format. 

---------------------------------------------------------------
#### modifylunassignments ####
Command:

    sfcli VolumeAccessGroup modifylunassignments <options>

Description:

The ModifyVolumeAccessGroupLunAssignments method enables you to define custom LUN assignments for specific volumes. This method changes only LUN values set on the lunAssignments parameter in the volume access group. All other LUN assignments remain unchanged. LUN assignment values must be unique for volumes in a volume access group. You cannot define duplicate LUN values within a volume access group. However, you can use the same LUN values again in different volume access groups.  Note: Correct LUN values are 0 through 16383. The system generates an exception if you pass a LUN value outside of this range. None of the specified LUN assignments are modified if there is an exception.  Caution: If you change a LUN assignment for a volume with active I/O, the I/O can be disrupted. You might need to change the server configuration before changing volume LUN assignments. 

Options:
--volumeaccessgroupid
The ID of the volume access group for which the LUN assignments will be modified. 

--lunassignments
The volume IDs with new assigned LUN values. 

--volumeid
The volume ID assigned to the Lun. 

--lun
Correct LUN values are 0 - 16383. An exception will be seen if an incorrect LUN value is passed. 

---------------------------------------------------------------
#### list ####
Command:

    sfcli VolumeAccessGroup list <options>

Description:

ListVolumeAccessGroups enables you to return information about the volume access groups that are currently in the system. 

Options:
--startvolumeaccessgroupid
The volume access group ID at which to begin the listing. If unspecified, there is no lower limit (implicitly 0). 

--limit
The maximum number of results to return. This can be useful for paging. 

--volumeaccessgroups
The list of ids of the volume access groups you wish to list 

---------------------------------------------------------------
#### getlunassignments ####
Command:

    sfcli VolumeAccessGroup getlunassignments <options>

Description:

The GetVolumeAccessGroupLunAssignments method enables you to retrieve details on LUN mappings of a specified volume access group. 

Options:
--volumeaccessgroupid
The unique volume access group ID used to return information. 

---------------------------------------------------------------
#### getefficiency ####
Command:

    sfcli VolumeAccessGroup getefficiency <options>

Description:

GetVolumeAccessGroupEfficiency enables you to retrieve efficiency information about a volume access group. Only the volume access group you provide as the parameter in this API method is used to compute the capacity. 

Options:
--volumeaccessgroupid
The volume access group for which capacity is computed. 


Restart Commands 
---------------------------------------------------------------
#### resetnode ####
Command:

    sfcli Restart resetnode <options>

Description:

The ResetNode API method enables you to reset a node to the factory settings. All data, packages (software upgrades, and so on), configurations, and log files are deleted from the node when you call this method. However, network settings for the node are preserved during this operation. Nodes that are participating in a cluster cannot be reset to the factory settings. The ResetNode API can only be used on nodes that are in an "Available" state. It cannot be used on nodes that are "Active" in a cluster, or in a "Pending" state. Caution: This method clears any data that is on the node. Exercise caution when using this method. Note: This method is available only through the per-node API endpoint 5.0 or later. 

Options:
--build
Specifies the URL to a remote Element software image to which the node will be reset. 

--force
Required parameter to successfully reset the node. 

---------------------------------------------------------------
#### networking ####
Command:

    sfcli Restart networking <options>

Description:

The RestartNetworking API method enables you to restart the networking services on a node. Warning: This method restarts all networking services on a node, causing temporary loss of networking connectivity. Exercise caution when using this method. Note: This method is available only through the per-node API endpoint 5.0 or later. 

Options:
--force
Required parameter to successfully reset the node. 

---------------------------------------------------------------
#### shutdown ####
Command:

    sfcli Restart shutdown <options>

Description:

The Shutdown API method enables you to restart or shutdown a node that has not yet been added to a cluster. To use this method, log in to the MIP for the pending node, and enter the "shutdown" method with either the "restart" or "halt" options. 

Options:
--nodes
List of NodeIDs for the nodes to be shutdown. 

--option
Specifies the action to take for the node shutdown. Possible values are: restart: Restarts the node. halt: Shuts down the node. 


Volume Commands 
---------------------------------------------------------------
#### listdeleted ####
Command:

    sfcli Volume listdeleted <options>

Description:

ListDeletedVolumes enables you to retrieve the list of volumes that have been marked for deletion and purged from the system. 

Options:
--includevirtualvolumes
Specifies that virtual volumes are included in the response by default. To exclude virtual volumes, set to false. 

---------------------------------------------------------------
#### liststatsby ####
Command:

    sfcli Volume liststatsby <options>

Description:

ListVolumeStatsByVolume returns high-level activity measurements for every volume, by volume. Values are cumulative from the creation of the volume. 

Options:
--includevirtualvolumes
Specifies that virtual volumes are included in the response by default. To exclude virtual volumes, set to false. 

---------------------------------------------------------------
#### create ####
Command:

    sfcli Volume create <options>

Description:

CreateVolume enables you to create a new (empty) volume on the cluster. As soon as the volume creation is complete, the volume is available for connection via iSCSI. 

Options:
--name
The name of the volume access group (might be user specified). Not required to be unique, but recommended. Might be 1 to 64 characters in length. 

--accountid
AccountID for the owner of this volume. 

--totalsize
Total size of the volume, in bytes. Size is rounded up to the nearest 1MB size. 

--enable512e
Specifies whether 512e emulation is enabled or not. Possible values are: true: The volume provides 512-byte sector emulation. false: 512e emulation is not enabled. 

--qosminiops
Desired minimum 4KB IOPS to guarantee. The allowed IOPS will only drop below this level if all volumes have been capped at their minimum IOPS value and there is still insufficient performance capacity. 

--qosmaxiops
Desired maximum 4KB IOPS allowed over an extended period of time. 

--qosburstiops
Maximum "peak" 4KB IOPS allowed for short periods of time. Allows for bursts of I/O activity over the normal max IOPS value. 

--qosbursttime
The length of time burst IOPS is allowed. The value returned is represented in time units of seconds. Note: this value is calculated by the system based on IOPS set for QoS. 

--attributes
The list of name-value pairs in JSON object format. Total attribute size must be less than 1000B, or 1KB, including JSON formatting characters. 

---------------------------------------------------------------
#### startbulkread ####
Command:

    sfcli Volume startbulkread <options>

Description:

StartBulkVolumeRead enables you to initialize a bulk volume read session on a specified volume. Only two bulk volume processes can run simultaneously on a volume. When you initialize the session, data is read from a SolidFire storage volume for the purposes of storing the data on an external backup source. The external data is accessed by a web server running on an SF-series node. Communications and server interaction information for external data access is passed by a script running on the storage system. At the start of a bulk volume read operation, a snapshot of the volume is made and the snapshot is deleted when the read is complete. You can also read a snapshot of the volume by entering the ID of the snapshot as a parameter. When you read a previous snapshot, the system does not create a new snapshot of the volume or delete the previous snapshot when the read completes. Note: This process creates a new snapshot if the ID of an existing snapshot is not provided. Snapshots can be created if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5. 

Options:
--volumeid
The ID of the volume to be read. 

--format
The format of the volume data. It can be either of the following formats: uncompressed: Every byte of the volume is returned without any compression. native: Opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write. 

--snapshotid
The ID of a previously created snapshot used for bulk volume reads. If no ID is entered, a snapshot of the current active volume image is made. 

--script
The executable name of a script. If unspecified, the key and URL is necessary to access SF-series nodes. The script is run on the primary node and the key and URL is returned to the script so the local web server can be contacted. 

--scriptparameters
JSON parameters to pass to the script. 

--attributes
JSON attributes for the bulk volume job. 

---------------------------------------------------------------
#### getefficiency ####
Command:

    sfcli Volume getefficiency <options>

Description:

GetVolumeEfficiency enables you to retrieve information about a volume. Only the volume you give as a parameter in this API method is used to compute the capacity. 

Options:
--volumeid
Specifies the volume for which capacity is computed. 

---------------------------------------------------------------
#### liststatsbyaccessgroup ####
Command:

    sfcli Volume liststatsbyaccessgroup <options>

Description:

ListVolumeStatsByVolumeAccessGroup enables you to get total activity measurements for all of the volumes that are a member of the specified volume access group(s). 

Options:
--volumeaccessgroups
An array of VolumeAccessGroupIDs for which volume activity is returned. If omitted, statistics for all volume access groups are returned. 

--includevirtualvolumes
Specifies that virtual volumes are included in the response by default. To exclude virtual volumes, set to false. 

---------------------------------------------------------------
#### listactive ####
Command:

    sfcli Volume listactive <options>

Description:

ListActiveVolumes enables you to return the list of active volumes currently in the system. The list of volumes is returned sorted in VolumeID order and can be returned in multiple parts (pages). 

Options:
--startvolumeid
Starting VolumeID to return. If no volume exists with this VolumeID, the next volume by VolumeID order is used as the start of the list. To page through the list, pass the VolumeID of the last volume in the previous response + 1. 

--limit
Maximum number of Volume Info objects to return. A value of 0 (zero) returns all volumes (unlimited). 

--includevirtualvolumes
Specifies that virtual volumes are included in the response by default. To exclude virtual volumes, set to false. 

---------------------------------------------------------------
#### liststatsbyaccount ####
Command:

    sfcli Volume liststatsbyaccount <options>

Description:

ListVolumeStatsByAccount returns high-level activity measurements for every account. Values are summed from all the volumes owned by the account. 

Options:
--accounts
One or more account ids by which to filter the result. 

--includevirtualvolumes
Includes virtual volumes in the response by default. To exclude virtual volumes, set to false. 

---------------------------------------------------------------
#### list ####
Command:

    sfcli Volume list <options>

Description:

The ListVolumes method enables you to retrieve a list of volumes that are in a cluster. You can specify the volumes you want to return in the list by using the available parameters. 

Options:
--startvolumeid
Only volumes with an ID greater than or equal to this value are returned. Mutually exclusive with the volumeIDs parameter. 

--limit
Specifies the maximum number of volume results that are returned. Mutually exclusive with the volumeIDs parameter. 

--volumestatus
Only volumes with a status equal to the status value are returned. Possible values are: creating snapshotting active deleted 

--accounts
Returns only the volumes owned by the accounts you specify here. Mutually exclusive with the volumeIDs parameter. 

--ispaired
Returns volumes that are paired or not paired. Possible values are: true: Returns all paired volumes. false: Returns all volumes that are not paired. 

--volumeids
A list of volume IDs. If you supply this parameter, other parameters operate only on this set of volumes. Mutually exclusive with the accounts, startVolumeID, and limit parameters. 

--volumename
Only volume object information matching the volume name is returned. 

--includevirtualvolumes
Specifies that virtual volumes are included in the response by default. To exclude virtual volumes, set to false. 

---------------------------------------------------------------
#### cancelclone ####
Command:

    sfcli Volume cancelclone <options>

Description:

CancelClone enables you to stop an ongoing CloneVolume or CopyVolume process. When you cancel a group clone operation, the system completes and removes the operation's associated asyncHandle. 

Options:
--cloneid
The cloneID for the ongoing clone process. 

---------------------------------------------------------------
#### liststats ####
Command:

    sfcli Volume liststats <options>

Description:

ListVolumeStats returns high-level activity measurements for a single volume, list of volumes, or all volumes (if you omit the volumeIDs parameter). Measurement values are cumulative from the creation of the volume. 

Options:
--volumeids
A list of volume IDs of volumes from which to retrieve activity information. 

---------------------------------------------------------------
#### getstats ####
Command:

    sfcli Volume getstats <options>

Description:

GetVolumeStats enables  you to retrieve high-level activity measurements for a single volume. Values are cumulative from the creation of the volume. 

Options:
--volumeid
Specifies the volume for which statistics are gathered. 

---------------------------------------------------------------
#### purgedeleted ####
Command:

    sfcli Volume purgedeleted <options>

Description:

PurgeDeletedVolume immediately and permanently purges a volume that has been deleted. You must delete a volume using DeleteVolume before it can be purged. Volumes are purged automatically after a period of time, so usage of this method is not typically required. 

Options:
--volumeid
The ID of the volume to be purged. 

---------------------------------------------------------------
#### getdefaultqos ####
Command:

    sfcli Volume getdefaultqos <options>

Description:

GetDefaultQoS enables you to retrieve the default QoS values for a newly created volume. 

Options:
---------------------------------------------------------------
#### delete ####
Command:

    sfcli Volume delete <options>

Description:

DeleteVolume marks an active volume for deletion. When marked, the volume is purged (permanently deleted) after the cleanup interval elapses. After making a request to delete a volume, any active iSCSI connections to the volume are immediately terminated and no further connections are allowed while the volume is in this state. A marked volume is not returned in target discovery requests. Any snapshots of a volume that has been marked for deletion are not affected. Snapshots are kept until the volume is purged from the system. If a volume is marked for deletion and has a bulk volume read or bulk volume write operation in progress, the bulk volume read or write operation is stopped. If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state. The remote volume that the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume. Until the deleted volume is purged, it can be restored and data transfers resume. If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed. The purged volume becomes permanently unavailable. 

Options:
--volumeid
The ID of the volume to be deleted. 

---------------------------------------------------------------
#### updatebulkstatus ####
Command:

    sfcli Volume updatebulkstatus <options>

Description:

You can use UpdateBulkVolumeStatus in a script to update the status of a bulk volume job that you started with the StartBulkVolumeRead or StartBulkVolumeWrite methods. 

Options:
--key
The key assigned during initialization of a StartBulkVolumeRead or StartBulkVolumeWrite session. 

--status
The status of the given bulk volume job. The system sets the status. Possible values are:  running: Jobs that are still active. complete: Jobs that are done. failed: Jobs that failed. 

--percentcomplete
The completed progress of the bulk volume job as a percentage value. 

--message
The message returned indicating the status of the bulk volume job after the job is complete. 

--attributes
JSON attributes; updates what is on the bulk volume job. 

---------------------------------------------------------------
#### removefromaccessgroup ####
Command:

    sfcli Volume removefromaccessgroup <options>

Description:

The RemoveVolumeFromVolumeAccessGroup method enables you to remove volumes from a volume access group. 

Options:
--volumeaccessgroupid
The ID of the volume access group to remove volumes from. 

--volumes
The ID of the volume access group to remove volumes from. 

---------------------------------------------------------------
#### copy ####
Command:

    sfcli Volume copy <options>

Description:

CopyVolume enables you to overwrite the data contents of an existing volume with the data contents of another volume (or snapshot). Attributes of the destination volume such as IQN, QoS settings, size, account, and volume access group membership are not changed. The destination volume must already exist and must be the same size as the source volume. NetApp strongly recommends that clients unmount the destination volume before the CopyVolume operation begins. If the destination volume is modified during the copy operation, the changes will be lost. This method is asynchronous and may take a variable amount of time to complete. You can use the GetAsyncResult method to determine when the process has finished, and ListSyncJobs to see the progress of the copy. 

Options:
--volumeid
VolumeID of the volume to be read from. 

--dstvolumeid
VolumeID of the volume to be overwritten. 

--snapshotid
ID of the snapshot that is used as the source of the clone. If no ID is provided, the current active volume is used. 

---------------------------------------------------------------
#### listbulkjobs ####
Command:

    sfcli Volume listbulkjobs <options>

Description:

ListBulkVolumeJobs enables you to retrieve information about each bulk volume read or write operation that is occurring in the system. 

Options:
---------------------------------------------------------------
#### addtoaccessgroup ####
Command:

    sfcli Volume addtoaccessgroup <options>

Description:

AddVolumesToVolumeAccessGroup enables you to add volumes to a specified volume access group. 

Options:
--volumeaccessgroupid
The ID of the volume access group to which volumes are added. 

--volumes
The list of volumes to add to the volume access group. 

---------------------------------------------------------------
#### startbulkwrite ####
Command:

    sfcli Volume startbulkwrite <options>

Description:

StartBulkVolumeWrite enables you to initialize a bulk volume write session on a specified volume. Only two bulk volume processes can run simultaneously on a volume. When you initialize the write session, data is written to a SolidFire storage volume from an external backup source. The external data is accessed by a web server running on an SF-series node. Communications and server interaction information for external data access is passed by a script running on the storage system. 

Options:
--volumeid
The ID of the volume to be written to. 

--format
The format of the volume data. It can be either of the following formats: uncompressed: Every byte of the volume is returned without any compression. native: Opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write. 

--script
The executable name of a script. If unspecified, the key and URL are necessary to access SF-series nodes. The script runs on the primary node and the key and URL is returned to the script, so the local web server can be contacted. 

--scriptparameters
JSON parameters to pass to the script. 

--attributes
JSON attributes for the bulk volume job. 

---------------------------------------------------------------
#### modify ####
Command:

    sfcli Volume modify <options>

Description:

ModifyVolume enables you to modify settings on an existing volume. You can make modifications to one volume at a time and changes take place immediately. If you do not specify QoS values when you modify a volume, they remain the same as before the modification. You can retrieve default QoS values for a newly created volume by running the GetDefaultQoS method. When you need to increase the size of a volume that is being replicated, do so in the following order to prevent replication errors: 1. Increase the size of the "Replication Target" volume. 2. Increase the size of the source or "Read / Write" volume. NetApp recommends that both the target and source volumes are the same size. Note: If you change the "access" status to locked or target, all existing iSCSI connections are terminated. 

Options:
--volumeid
VolumeID for the volume to be modified. 

--accountid
AccountID to which the volume is reassigned. If unspecified, the previous account name is used. 

--access
Specifies the access allowed for the volume. Possible values are: readOnly: Only read operations are allowed. readWrite: Reads and writes are allowed. locked: No reads or writes are allowed. If not specified, the access value does not change. replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked. If a value is not specified, the access value does not change. 

--qosminiops
Desired minimum 4KB IOPS to guarantee. The allowed IOPS will only drop below this level if all volumes have been capped at their minimum IOPS value and there is still insufficient performance capacity. 

--qosmaxiops
Desired maximum 4KB IOPS allowed over an extended period of time. 

--qosburstiops
Maximum "peak" 4KB IOPS allowed for short periods of time. Allows for bursts of I/O activity over the normal max IOPS value. 

--qosbursttime
The length of time burst IOPS is allowed. The value returned is represented in time units of seconds. Note: this value is calculated by the system based on IOPS set for QoS. 

--totalsize
New size of the volume in bytes. 1000000000 is equal to 1GB. Size is rounded up to the nearest 1MB. This parameter can only be used to increase the size of a volume. 

--attributes
List of name-value pairs in JSON object format. 

---------------------------------------------------------------
#### getcount ####
Command:

    sfcli Volume getcount <options>

Description:

GetVolumeCount enables you to retrieve the number of volumes currently in the system. 

Options:
---------------------------------------------------------------
#### cancelgroupclone ####
Command:

    sfcli Volume cancelgroupclone <options>

Description:

CancelGroupClone enables you to stop an ongoing CloneMultipleVolumes process occurring on a group of volumes. When you cancel a group clone operation, the system completes and removes the operation's associated asyncHandle. 

Options:
--groupcloneid
The cloneID for the ongoing clone process. 

---------------------------------------------------------------
#### setdefaultqos ####
Command:

    sfcli Volume setdefaultqos <options>

Description:

SetDefaultQoS enables you to configure the default Quality of Service (QoS) values (measured in inputs and outputs per second, or IOPS) for a volume. For more information about QoS in a SolidFire cluster, see the User Guide. 

Options:
--miniops
The minimum number of sustained IOPS provided by the cluster to a volume. 

--maxiops
The maximum number of sustained IOPS provided by the cluster to a volume. 

--burstiops
The maximum number of IOPS allowed in a short burst scenario. 

---------------------------------------------------------------
#### listforaccount ####
Command:

    sfcli Volume listforaccount <options>

Description:

ListVolumesForAccount returns the list of active and (pending) deleted volumes for an account. 

Options:
--accountid
Returns all volumes owned by this AccountID. 

--startvolumeid
The ID of the first volume to list. This can be useful for paging results. By default, this starts at the lowest VolumeID. 

--limit
The maximum number of volumes to return from the API. 

--includevirtualvolumes
Specifies that virtual volumes are included in the response by default. To exclude virtual volumes, set to false. 

---------------------------------------------------------------
#### clonemultiple ####
Command:

    sfcli Volume clonemultiple <options>

Description:

CloneMultipleVolumes enables you to create a clone of a group of specified volumes. You can assign a consistent set of characteristics to a group of multiple volumes when they are cloned together. Before using groupSnapshotID to clone the volumes in a group snapshot, you must create the group snapshot by using the CreateGroupSnapshot API method or the Element OS Web UI. Using groupSnapshotID is optional when cloning multiple volumes. Note: Cloning multiple volumes is allowed if cluster fullness is at stage 2 or 3. Clones are not created when cluster fullness is at stage 4 or 5. 

Options:
--volumes
Unique ID for each volume to include in the clone. If optional parameters are not specified, the values are inherited from the source volumes. Required parameter for "volumes" array: volumeID Optional parameters for "volumes" array: access: Can be one of readOnly, readWrite, locked, or replicationTarget attributes: List of name-value pairs in JSON object format. name: New name for the clone. newAccountID: Account ID for the new volumes. newSize: New size Total size of the volume, in bytes. Size is rounded up to the nearest 1MB. 

--volumeid
Required parameter for "volumes" array: volumeID. 

--accessvolumes
Access settings for the new volume. readOnly: Only read operations are allowed. readWrite: Reads and writes are allowed. locked: No reads or writes are allowed. replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.  If unspecified, the access settings of the clone will be the same as the source. 

--name
New name for the clone. 

--newaccountidvolumes
Account ID for the new volume. 

--newsize
New size Total size of the volume, in bytes. Size is rounded up to the nearest 1MB size. 

--attributes
List of Name/Value pairs in JSON object format. 

--access
New default access method for the new volumes if not overridden by information passed in the volume's array. 

--groupsnapshotid
ID of the group snapshot to use as a basis for the clone. 

--newaccountid
New account ID for the volumes if not overridden by information passed in the volumes array. 

---------------------------------------------------------------
#### clone ####
Command:

    sfcli Volume clone <options>

Description:

CloneVolume enables you to create a copy of a volume. This method is asynchronous and might take a variable amount of time to complete. The cloning process begins immediately when you make the CloneVolume request and is representative of the state of the volume when the API method is issued. You can use the GetAsyncResult method to determine when the cloning process is complete and the new volume is available for connections. You can use ListSyncJobs to see the progress of creating the clone. Note: The initial attributes and QoS settings for the volume are inherited from the volume being cloned. You can change these settings with ModifyVolume. Note: Cloned volumes do not inherit volume access group memberships from the source volume. 

Options:
--volumeid
VolumeID for the volume to be cloned. 

--name
The name of the new cloned volume. Might be 1 to 64 characters in length. 

--newaccountid
AccountID for the owner of the new volume. If unspecified, the accountID of the owner of the volume being cloned is used. 

--newsize
New size of the volume, in bytes. Might be greater or less than the size of the volume being cloned. If unspecified, the volume size is not changed. Size is rounded to the nearest 1MB. 

--access
Specifies the level of access allowed for the new volume. Possible values are: readOnly: Only read operations are allowed. readWrite: Reads and writes are allowed. locked: No reads or writes are allowed. If unspecified, the level of access of the volume being cloned is used. replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked. If a value is not specified, the access value does not change. 

--snapshotid
ID of the snapshot that is used as the source of the clone. If no ID is provided, the current active volume is used. 

--attributes
List of name-value pairs in JSON object format. 

--enable512e
Should the volume provide 512-byte sector emulation? 

---------------------------------------------------------------
#### restoredeleted ####
Command:

    sfcli Volume restoredeleted <options>

Description:

RestoreDeletedVolume marks a deleted volume as active again. This action makes the volume immediately available for iSCSI connection. 

Options:
--volumeid
VolumeID of the deleted volume to be restored. 


Node Commands 
---------------------------------------------------------------
#### listall ####
Command:

    sfcli Node listall <options>

Description:

ListAllNodes enables you to retrieve a list of active and pending nodes in the cluster. 

Options:
---------------------------------------------------------------
#### getorigin ####
Command:

    sfcli Node getorigin <options>

Description:

GetOrigin enables you to retrieve the origination certificate for where the node was built. This method might return null if there is no origination certification. 

Options:
---------------------------------------------------------------
#### listactive ####
Command:

    sfcli Node listactive <options>

Description:

ListActiveNodes returns the list of currently active nodes that are in the cluster. 

Options:
---------------------------------------------------------------
#### listpendingactive ####
Command:

    sfcli Node listpendingactive <options>

Description:

ListPendingActiveNodes returns the list of nodes in the cluster that are currently in the PendingActive state, between the pending and active states. These are nodes that are currently being returned to the factory image. 

Options:
---------------------------------------------------------------

# Set config has been omitted from this cli

---------------------------------------------------------------
#### remove ####
Command:

    sfcli Node remove <options>

Description:

You can use RemoveNodes to remove one or more nodes that should no longer participate in the cluster. Before removing a node, you must remove all drives the node contains using the RemoveDrives method. You cannot remove a node until the RemoveDrives process has completed and all data has been migrated away from the node. After you remove a node, it registers itself as a pending node. You can add the node again or shut it down (shutting the node down removes it from the Pending Node list). 

Options:
--nodes
List of NodeIDs for the nodes to be removed. 

---------------------------------------------------------------
#### listpending ####
Command:

    sfcli Node listpending <options>

Description:

ListPendingNodes returns a list of the currently pending nodes in the system. Pending nodes are nodes that are running and configured to join the cluster, but have not yet been added via the AddNodes API method. 

Options:
---------------------------------------------------------------

# Set network config has been omitted from this cli

---------------------------------------------------------------
#### getconfig ####
Command:

    sfcli Node getconfig <options>

Description:

The GetConfig API method enables you to retrieve all configuration information for a node. This method includes the same information available in both the GetClusterConfig and GetNetworkConfig API methods. Note: This method is available only through the per-node API endpoint 5.0 or later. 

Options:
---------------------------------------------------------------
#### getbootstrapconfig ####
Command:

    sfcli Node getbootstrapconfig <options>

Description:

GetBootstrapConfig returns cluster and node information from the bootstrap configuration file. Use this API method on an individual node before it has been joined with a cluster. You can use the information this method returns in the cluster configuration interface when you create a cluster. 

Options:
---------------------------------------------------------------
#### getpendingoperation ####
Command:

    sfcli Node getpendingoperation <options>

Description:

You can use GetPendingOperation to detect an operation on a node that is currently in progress. You can also use this method to report back when an operation has completed.  Note: method is available only through the per-node API endpoint 5.0 or later. 

Options:
---------------------------------------------------------------
#### getstats ####
Command:

    sfcli Node getstats <options>

Description:

GetNodeStats enables you to retrieve the high-level activity measurements for a single node. 

Options:
--nodeid
Specifies the node for which statistics are gathered. 

---------------------------------------------------------------
#### liststats ####
Command:

    sfcli Node liststats <options>

Description:

ListNodeStats enables you to view the high-level activity measurements for all nodes in a cluster. 

Options:
---------------------------------------------------------------
#### getnetworkconfig ####
Command:

    sfcli Node getnetworkconfig <options>

Description:

The GetNetworkConfig API method enables you to display the network configuration information for a node. Note: This method is available only through the per-node API endpoint 5.0 or later. 

Options:
---------------------------------------------------------------
#### add ####
Command:

    sfcli Node add <options>

Description:

AddNodes enables you to add one or more new nodes to a cluster. When a node that is not configured starts up for the first time, you are prompted to configure the node. After you configure the node, it is registered as a "pending node" with the cluster.  Note: It might take several seconds after adding a new node for it to start up and register its drives as available. 

Options:
--pendingnodes
 List of pending NodeIDs for the nodes to be added. You can  obtain the list of pending nodes using the ListPendingNodes method. 

--autoinstall
Whether these nodes should be autoinstalled 


Logging Commands 
---------------------------------------------------------------
#### setloginsessioninfo ####
Command:

    sfcli Logging setloginsessioninfo <options>

Description:

You can use SetLoginSessionInfo to set the period of time that a session's login authentication is valid. After the log in period elapses without activity on the system, the authentication expires. New login credentials are required for continued access to the cluster after the timeout period has elapsed. 

Options:
--timeout
Cluster authentication expiration period. Formatted in HH:mm:ss. For example, 01:30:00, 00:90:00, and 00:00:5400 can be used to equal a 90 minute timeout period. The default value is 30 minutes. 

---------------------------------------------------------------
#### getloginsessioninfo ####
Command:

    sfcli Logging getloginsessioninfo <options>

Description:

GetLoginSessionInfo enables you to return the period of time a log in authentication session is valid for both log in shells and the TUI. 

Options:
---------------------------------------------------------------
#### getremotehosts ####
Command:

    sfcli Logging getremotehosts <options>

Description:

GetRemoteLoggingHosts enables you to retrieve the current list of log servers. 

Options:
---------------------------------------------------------------
#### setremotehosts ####
Command:

    sfcli Logging setremotehosts <options>

Description:

SetRemoteLoggingHosts enables you to configure remote logging from the nodes in the storage cluster to a centralized log server or servers. Remote logging is performed over TCP using the default port 514. This API does not add to the existing logging hosts. Rather, it replaces what currently exists with new values specified by this API method. You can use GetRemoteLoggingHosts to determine what the current logging hosts are, and then use SetRemoteLoggingHosts to set the desired list of current and new logging hosts. 

Options:
--remotehosts
A list of hosts to send log messages to. 

--host
Hostname or IP address of the log server. 

--port
Port number that the log server is listening on. 


Account Commands 
---------------------------------------------------------------
#### modify ####
Command:

    sfcli Account modify <options>

Description:

ModifyAccount enables you to modify an existing account. When you lock an account, any existing connections from that account are immediately terminated. When you change an account's CHAP settings, any existing connections remain active, and the new CHAP settings are used on subsequent connections or reconnections. To clear an account's attributes, specify {} for the attributes parameter. 

Options:
--accountid
Specifies the AccountID for the account to be modified. 

--username
Specifies the username associated with the account. (Might be 1 to 64 characters in length). 

--status
Sets the status for the account. Possible values are: active: The account is active and connections are allowed. locked: The account is locked and connections are refused. 

--initiatorsecret
Specifies the CHAP secret to use for the initiator. This secret must be 12-16 characters in length and should be impenetrable. The initiator CHAP secret must be unique and cannot be the same as the target CHAP secret. 

--targetsecret
Specifies the CHAP secret to use for the target (mutual CHAP authentication). This secret must be 12-16 characters in length and should be impenetrable. The target CHAP secret must be unique and cannot be the same as the initiator CHAP secret. 

--attributes
List of name-value pairs in JSON object format. 

---------------------------------------------------------------
#### remove ####
Command:

    sfcli Account remove <options>

Description:

RemoveAccount enables you to remove an existing account. You must delete and purge all volumes associated with the account using DeleteVolume before you can remove the account. If volumes on the account are still pending deletion, you cannot use RemoveAccount to remove the account. 

Options:
--accountid
Specifies the AccountID for the account to be removed. 

---------------------------------------------------------------
#### add ####
Command:

    sfcli Account add <options>

Description:

You can use AddAccount to add a new account to the system. You can create new volumes under the new account. The CHAP settings you specify for the account apply to all volumes owned by the account. 

Options:
--username
Specifies the username for this account. (Might be 1 to 64 characters in length). 

--initiatorsecret
The CHAP secret to use for the initiator. This secret must be 12-16 characters in length and should be impenetrable. The initiator CHAP secret must be unique and cannot be the same as the target CHAP secret. If unspecified, a random secret is created. 

--targetsecret
The CHAP secret to use for the target (mutual CHAP authentication). This secret must be 12-16 characters in length and should be impenetrable. The target CHAP secret must be unique and cannot be the same as the initiator CHAP secret. If unspecified, a random secret is created. 

--attributes
List of name-value pairs in JSON object format. 

---------------------------------------------------------------
#### list ####
Command:

    sfcli Account list <options>

Description:

ListAccounts returns the entire list of accounts, with optional paging support. 

Options:
--startaccountid
Starting AccountID to return. If no account exists with this AccountID, the next account by AccountID order is used as the start of the list. To page through the list, pass the AccountID of the last account in the previous response + 1. 

--limit
Maximum number of AccountInfo objects to return. 

--includestoragecontainers
Includes storage containers in the response by default. To exclude storage containers, set to false. 

---------------------------------------------------------------
#### getbyname ####
Command:

    sfcli Account getbyname <options>

Description:

GetAccountByName enables you to retrieve details about a specific account, given its username. 

Options:
--username
Username for the account. 

---------------------------------------------------------------
#### getefficiency ####
Command:

    sfcli Account getefficiency <options>

Description:

GetAccountEfficiency enables you to retrieve efficiency statistics about a volume account. This method returns efficiency information only for the account you specify as a parameter. 

Options:
--accountid
Specifies the volume account for which efficiency statistics are returned. 

---------------------------------------------------------------
#### getbyid ####
Command:

    sfcli Account getbyid <options>

Description:

GetAccountByID enables you to return details about a specific account, given its accountID. 

Options:
--accountid
Specifies the account for which details are gathered. 


BackupTarget Commands 
---------------------------------------------------------------
#### get ####
Command:

    sfcli BackupTarget get <options>

Description:

GetBackupTarget enables you to return information about a specific backup target that you have created. 

Options:
--backuptargetid
The unique identifier assigned to the backup target. 

---------------------------------------------------------------
#### modify ####
Command:

    sfcli BackupTarget modify <options>

Description:

ModifyBackupTarget enables you to change attributes of a backup target. 

Options:
--backuptargetid
The unique target ID for the target to modify. 

--name
The new name for the backup target. 

--attributes
List of name-value pairs in JSON object format. 

---------------------------------------------------------------
#### list ####
Command:

    sfcli BackupTarget list <options>

Description:

You can use ListBackupTargets to retrieve information about all backup targets that have been created. 

Options:
---------------------------------------------------------------
#### create ####
Command:

    sfcli BackupTarget create <options>

Description:

CreateBackupTarget enables you to create and store backup target information so that you do not need to re-enter it each time a backup is created. 

Options:
--name
The name of the backup target. 

--attributes
List of name-value pairs in JSON object format. 

---------------------------------------------------------------
#### remove ####
Command:

    sfcli BackupTarget remove <options>

Description:

RemoveBackupTarget allows you to delete backup targets. 

Options:
--backuptargetid
The unique target ID of the target to remove. 


Service Commands 
---------------------------------------------------------------
#### list ####
Command:

    sfcli Service list <options>

Description:

You can use ListServices to return the services information for nodes, drives, current software, and other services that are running on the cluster. 

Options:
---------------------------------------------------------------
#### restart ####
Command:

    sfcli Service restart <options>

Description:

The RestartServices API method enables you to restart the services on a node. Caution: This method causes temporary node services interruption. Exercise caution when using this method. Note: This method is available only through the per-node API endpoint 5.0 or later. 

Options:
--force
Required parameter to successfully restart services on a node. 

--service
Service name to be restarted. 

--action
Action to perform on the service (start, stop, restart). 


Schedule Commands 
---------------------------------------------------------------
#### get ####
Command:

    sfcli Schedule get <options>

Description:

You can use the GetSchedule method to retrieve information about a scheduled snapshot. You can see information about a specific schedule if there are many snapshot schedules in the system. You also retrieve information about more than one schedule with this method by specifying additional scheduleIDs in the parameter. 

Options:
--scheduleid
Specifies the unique ID of the schedule or multiple schedules to display. 

---------------------------------------------------------------
#### modifyschedule ####
Command:

    sfcli Snapshot modifyschedule <options>

Description:

ModifySchedule enables you to change the intervals at which a scheduled snapshot occurs. This allows for adjustment to the snapshot frequency and retention. 

Options:
--name
Unique name assigned to the schedule.

--minutes
If provided with hours and days, it suggests (with hours and days) how much time is in between each snapshot. If it is provided with weekdays or monthdays, it suggests the time on which a snapshot will occur. If not provided, defaults to 0.

--hours
If provided with minutes and days, it suggests (with minutes and days) how much time is in between each snapshot. If it is provided with weekdays or monthdays, it suggests the time on which a snapshot will occur.

--days
Indicates the number of days in between each snapshot.

--weekdays
Indicates the weekday on which the snapshot will occur.

--monthdays
Indicates the monthdays on which snapshots will occur..

--scheduleid
Unique ID of the schedule

--recurring
Indicates whether or not the schedule is recurring.

--tobedeleted
Indicates if the schedule is marked for deletion.

--paused
Indicates whether or not the schedule is paused.

--startingdate
Indicates the date the first time the schedule began of will begin. Formatted in UTC time.

--haserror
Indicates whether or not the schedule has errors.

--runnextinterval
Indicates whether or not the schedule will run the next time the scheduler is active. When set to "true", the schedule will run the next time the scheduler is active and then reset back to "false".

--lastruntimestarted
Indicates the last time the schedule started n ISO 8601 date string. Valid values are: Success Failed

--lastrunstatus
Indicates the status of the last scheduled snapshot. Valid values are: Success Failed


---------------------------------------------------------------
#### list ####
Command:

    sfcli Schedule list <options>

Description:

ListSchedule enables you to retrieve information about all scheduled snapshots that have been created. 

Options:
---------------------------------------------------------------
#### createschedule ####
Command:

    sfcli Snapshot createschedule <options>

Description:

CreateSchedule enables you to schedule an automatic snapshot of a volume at a defined interval. You can use the created snapshot later as a backup or rollback to ensure the data on a volume or group of volumes is consistent for the point in time in which the snapshot was created. If you schedule a snapshot to run at a time period that is not divisible by 5 minutes, the snapshot runs at the next time period that is divisible by 5 minutes. For example, if you schedule a snapshot to run at 12:42:00 UTC, it runs at 12:45:00 UTC. Note: You can create snapshots if cluster fullness is at stage 1, 2 or 3. You cannot create snapshots after cluster fullness reaches stage 4 or 5.

Options:
--name
Unique name assigned to the schedule.

--minutes
If provided with hours and days, it suggests (with hours and days) how much time is in between each snapshot. If it is provided with weekdays or monthdays, it suggests the time on which a snapshot will occur. If not provided, defaults to 0.

--hours
If provided with minutes and days, it suggests (with minutes and days) how much time is in between each snapshot. If it is provided with weekdays or monthdays, it suggests the time on which a snapshot will occur.

--days
Indicates the number of days in between each snapshot.

--weekdays
Indicates the weekday on which the snapshot will occur.

--monthdays
Indicates the monthdays on which snapshots will occur..

--scheduleid
Unique ID of the schedule

--recurring
Indicates whether or not the schedule is recurring.

--tobedeleted
Indicates if the schedule is marked for deletion.

--paused
Indicates whether or not the schedule is paused.

--startingdate
Indicates the date the first time the schedule began of will begin. Formatted in UTC time.

--haserror
Indicates whether or not the schedule has errors.

--runnextinterval
Indicates whether or not the schedule will run the next time the scheduler is active. When set to "true", the schedule will run the next time the scheduler is active and then reset back to "false".

--lastruntimestarted
Indicates the last time the schedule started n ISO 8601 date string. Valid values are: Success Failed

--lastrunstatus
Indicates the status of the last scheduled snapshot. Valid values are: Success Failed



LDAP Commands 
---------------------------------------------------------------
#### enableauthentication ####
Command:

    sfcli LDAP enableauthentication <options>

Description:

The EnableLdapAuthentication method enables you to configure an LDAP directory connection to use for LDAP authentication to a cluster. Users that are members of the LDAP directory can then log in to the storage system using their LDAP credentials. 

Options:
--serveruris
A comma-separated list of LDAP server URIs (examples: "ldap://1.2.3.4" and ldaps://1.2.3.4:123") 

--authtype
Identifies which user authentication method to use. Must be one of the following: DirectBind SearchAndBind 

--groupsearchbasedn
The base DN of the tree to start the group search (will do a subtree search from here). 

--groupsearchcustomfilter
For use with the CustomFilter search type, an LDAP filter to use to return the DNs of a users groups. The string can have placeholder text of %USERNAME% and %USERDN% to be replaced with their username and full userDN as needed. 

--groupsearchtype
Controls the default group search filter used, and must be one of the following: NoGroups: No group support. ActiveDirectory: Nested membership of all of a users AD groups. MemberDN: MemberDN style groups (single level). 

--searchbinddn
A fully qualified DN to log in with to perform an LDAP search for the user (needs read access to the LDAP directory). 

--searchbindpassword
The password for the searchBindDN account used for searching. 

--userdntemplate
A string that is used to form a fully qualified user DN. The string should have the placeholder text %USERNAME%, which is replaced with the username of the authenticating user. 

--usersearchbasedn
The base DN of the tree to start the search (will do a subtree search from here). 

--usersearchfilter
The LDAP filter to use. The string should have the placeholder text %USERNAME% which is replaced with the username of the authenticating user. Example: (&(objectClass=person)(sAMAccountName=%USERNAME%)) will use the sAMAccountName field in Active Directory to match the username entered at cluster login. 

---------------------------------------------------------------
#### disableauthentication ####
Command:

    sfcli LDAP disableauthentication <options>

Description:

The DisableLdapAuthentication method enables you to disable LDAP authentication and remove all LDAP configuration settings. This method does not remove any configured cluster admin accounts (user or group). However, those cluster admin accounts will no longer be able to log in. 

Options:
---------------------------------------------------------------
#### getconfiguration ####
Command:

    sfcli LDAP getconfiguration <options>

Description:

The GetLdapConfiguration method enables you to get the currently active LDAP configuration on the cluster. 

Options:
---------------------------------------------------------------
#### testauthentication ####
Command:

    sfcli LDAP testauthentication <options>

Description:

The TestLdapAuthentication method enables you to validate the currently enabled LDAP authentication settings. If the configuration is correct, the API call returns the group membership of the tested user. 

Options:
--username
The username to be tested. 

--password
The password for the username to be tested. 

--ldapconfigurationauthtype
Identifies which user authentcation method will be used.  Valid values: DirectBind SearchAndBind 

--ldapconfigurationenabled
Identifies whether or not the system is enabled for LDAP.  Valid values: true false 

--ldapconfigurationgroupsearchbasedn
The base DN of the tree to start the group search (will do a subtree search from here). 

--ldapconfigurationgroupsearchcustomfilter
The custom search filter used. 

--ldapconfigurationgroupsearchtype
Controls the default group search filter used, can be one of the following: NoGroups: No group support. ActiveDirectory: Nested membership of all of a user's AD groups. MemberDN: MemberDN style groups (single-level). 

--ldapconfigurationsearchbinddn
A fully qualified DN to log in with to perform an LDAP search for the user (needs read access to the LDAP directory). 

--ldapconfigurationserveruris
A comma-separated list of LDAP server URIs (examples: "ldap://1.2.3.4" and ldaps://1.2.3.4:123") 

--ldapconfigurationuserdntemplate
A string that is used to form a fully qualified user DN. 

--ldapconfigurationusersearchbasedn
The base DN of the tree used to start the search (will do a subtree search from here). 

--ldapconfigurationusersearchfilter
The LDAP filter used. 

---------------------------------------------------------------
#### addclusteradmin ####
Command:

    sfcli LDAP addclusteradmin <options>

Description:

AddLdapClusterAdmin enables you to add a new LDAP cluster administrator user. An LDAP cluster administrator can manage the cluster via the API and management tools. LDAP cluster admin accounts are completely separate and unrelated to standard tenant accounts. You can also use this method to add an LDAP group that has been defined in Active Directory. The access level that is given to the group is passed to the individual users in the LDAP group. 

Options:
--username
The distinguished user name for the new LDAP cluster admin. 

--access
Controls which methods this Cluster Admin can use. For more details on the levels of access, see the Access Control appendix in the SolidFire API Reference. 

--accepteula
Accept the End User License Agreement. Set to true to add a cluster administrator account to the system. If omitted or set to false, the method call fails. 

--attributes
List of name-value pairs in JSON object format. 


Pairing Commands 
---------------------------------------------------------------
#### removevolumepair ####
Command:

    sfcli Pairing removevolumepair <options>

Description:

RemoveVolumePair enables you to remove the remote pairing between two volumes. Use this method on both the source and target volumes that are paired together. When you remove the volume pairing information, data is no longer replicated to or from the volume. 

Options:
--volumeid
The ID of the volume on which to stop the replication process. 

---------------------------------------------------------------
#### completevolume ####
Command:

    sfcli Pairing completevolume <options>

Description:

You can use the CompleteVolumePairing method to complete the pairing of two volumes. 

Options:
--volumepairingkey
The key returned from the StartVolumePairing method. 

--volumeid
The ID of the volume on which to complete the pairing process. 

---------------------------------------------------------------
#### completecluster ####
Command:

    sfcli Pairing completecluster <options>

Description:

You can use the CompleteClusterPairing method with the encoded key received from the  StartClusterPairing method to complete the cluster pairing process. The CompleteClusterPairing method is the second step in the cluster pairing process.  

Options:
--clusterpairingkey
A string of characters that is returned from the "StartClusterPairing" API method. 

---------------------------------------------------------------
#### listactivepairedvolumes ####
Command:

    sfcli Pairing listactivepairedvolumes <options>

Description:

ListActivePairedVolumes enables you to list all the active volumes paired with a volume. This method returns information about volumes with active and pending pairings. 

Options:
--startvolumeid
The beginning of the range of active paired volumes to return. 

--limit
Maximum number of active paired volumes to return. 

---------------------------------------------------------------
#### startvolume ####
Command:

    sfcli Pairing startvolume <options>

Description:

StartVolumePairing enables you to create an encoded key from a volume that is used to pair with another volume. The key that this method creates is used in the CompleteVolumePairing API method to establish a volume pairing. 

Options:
--volumeid
The ID of the volume on which to start the pairing process. 

--mode
The mode of the volume on which to start the pairing process. The mode can only be set if the volume is the source volume. Possible values are: Async: (default if no mode parameter specified) Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster. Sync: Source acknowledges write when the data is stored locally and on the remote cluster. SnapshotsOnly: Only snapshots created on the source cluster will be replicated. Active writes from the source volume are not replicated. 

---------------------------------------------------------------
#### startcluster ####
Command:

    sfcli Pairing startcluster <options>

Description:

You can use the StartClusterPairing method to create an encoded key from a cluster that is used to pair with another cluster. The key created from this API method is used in the CompleteClusterPairing API method to establish a cluster pairing. You can pair a cluster with a maximum of four other clusters.  

Options:
---------------------------------------------------------------
#### removeclusterpair ####
Command:

    sfcli Pairing removeclusterpair <options>

Description:

You can use the RemoveClusterPair method to close the open connections between two paired clusters. Note: Before you remove a cluster pair, you must first remove all volume pairing to the clusters with the "RemoveVolumePair" API method. 

Options:
--clusterpairid
Unique identifier used to pair two clusters. 

---------------------------------------------------------------
#### modifyvolumepair ####
Command:

    sfcli Pairing modifyvolumepair <options>

Description:

ModifyVolumePair enables you to pause or restart replication between a pair of volumes. 

Options:
--volumeid
The ID of the volume to be modified. 

--pausedmanual
Specifies whether to pause or restart volume replication process. Valid values are:  true: Pauses volume replication false: Restarts volume replication 

--mode
Specifies the volume replication mode. Possible values are: Async: Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster. Sync: The source acknowledges the write when the data is stored locally and on the remote cluster. SnapshotsOnly: Only snapshots created on the source cluster are replicated. Active writes from the source volume are not replicated. 

--pauselimit
Internal use only. 

---------------------------------------------------------------
#### listclusterpairs ####
Command:

    sfcli Pairing listclusterpairs <options>

Description:

You can use the ListClusterPairs method to list all the clusters that a cluster is paired with. This method returns information about active and pending cluster pairings, such as statistics about the current pairing as well as the connectivity and latency (in milliseconds) of the cluster pairing. 

Options:

Initiators Commands 
---------------------------------------------------------------
#### modify ####
Command:

    sfcli Initiators modify <options>

Description:

ModifyInitiators enables you to change the attributes of one or more existing initiators. You cannot change the name of an existing initiator. If you need to change the name of an initiator, delete it first with DeleteInitiators and create a new one with CreateInitiators. If ModifyInitiators fails to change one of the initiators provided in the parameter, the method returns an error and does not modify any initiators (no partial completion is possible). 

Options:
--initiators
A list of objects containing characteristics of each initiator to modify. Values are: initiatorID: (Required) The ID of the initiator to modify. (Integer) alias: (Optional) A new friendly name to assign to the initiator. (String) attributes: (Optional) A new set of JSON attributes to assign to the initiator. (JSON Object) volumeAccessGroupID: (Optional) The ID of the volume access group into to which the initiator should be added. If the initiator was previously in a different volume access group, it is removed from the old volume access group. If this key is present but null, the initiator is removed from its current volume access group, but not placed in any new volume access group. (Integer) 

--initiatorid
(Required) The numeric ID of the initiator to modify. (Integer) 

--alias
(Optional) A new friendly name to assign to the initiator. (String) 

--volumeaccessgroupid
(Optional) The ID of the volume access group to which the newly created initiator should be added. If the initiator was previously in a different volume access group, it is removed from the old volume access group. If this key is present but null, the initiator is removed from its current volume access group, but not placed in any new volume access group. (Integer) 

--attributes
(Optional) A new set of JSON attributes assigned to this initiator. (JSON Object) 

---------------------------------------------------------------
#### delete ####
Command:

    sfcli Initiators delete <options>

Description:

DeleteInitiators enables you to delete one or more initiators from the system (and from any associated volumes or volume access groups). If DeleteInitiators fails to delete one of the initiators provided in the parameter, the system returns an error and does not delete any initiators (no partial completion is possible). 

Options:
--initiators
An array of IDs of initiators to delete. 

---------------------------------------------------------------
#### addtovolumeaccessgroup ####
Command:

    sfcli Initiators addtovolumeaccessgroup <options>

Description:

AddInitiatorsToVolumeAccessGroup enables you to add initiators to a specified volume access group. 

Options:
--volumeaccessgroupid
The ID of the volume access group to modify. 

--initiators
The list of initiators to add to the volume access group. 

---------------------------------------------------------------
#### list ####
Command:

    sfcli Initiators list <options>

Description:

ListInitiators enables you to list initiator IQNs or World Wide Port Names (WWPNs). 

Options:
--startinitiatorid
The initiator ID at which to begin the listing. You can supply this parameter or the "initiators" parameter, but not both. 

--limit
The maximum number of initiator objects to return. 

--initiators
A list of initiator IDs to retrieve. You can provide a value for this parameter or the "startInitiatorID" parameter, but not both. 

---------------------------------------------------------------
#### removefromvolumeaccessgroup ####
Command:

    sfcli Initiators removefromvolumeaccessgroup <options>

Description:

RemoveInitiatorsFromVolumeAccessGroup enables you to remove initiators from a specified volume access group. 

Options:
--volumeaccessgroupid
The ID of the volume access group from which the initiators are removed. 

--initiators
The list of initiators to remove from the volume access group. 

--deleteorphaninitiators
true: Delete initiator objects after they are removed from a volume access group. false: Do not delete initiator objects after they are removed from a volume access group. 

---------------------------------------------------------------
#### create ####
Command:

    sfcli Initiators create <options>

Description:

CreateInitiators enables you to create multiple new initiator IQNs or World Wide Port Names (WWPNs) and optionally assign them aliases and attributes. When you use CreateInitiators to create new initiators, you can also add them to volume access groups. If CreateInitiators fails to create one of the initiators provided in the parameter, the method returns an error and does not create any initiators (no partial completion is possible). 

Options:
--initiators
A list of objects containing characteristics of each new initiator. Values are: name: (Required) The name of the initiator (IQN or WWPN) to create. (String) alias: (Optional) The friendly name to assign to this initiator. (String) attributes: (Optional) A set of JSON attributes to assign to this initiator. (JSON Object) volumeAccessGroupID: (Optional) The ID of the volume access group into to which this newly created initiator will be added. (Integer) 

--name
(Required) The name of the initiator (IQN or WWPN) to create. (String) 

--alias
(Optional) The friendly name to assign to this initiator. (String) 

--volumeaccessgroupid
(Optional) The ID of the volume access group to which this newly created initiator will be added. (Integer) 

--attributes
(Optional) A set of JSON attributes assigned to this initiator. (JSON Object) 


Drive Commands 
---------------------------------------------------------------
#### remove ####
Command:

    sfcli Drive remove <options>

Description:

You can use RemoveDrives to proactively remove drives that are part of the cluster. You might want to use this method when reducing cluster capacity or preparing to replace drives nearing the end of their service life. Any data on the drives is removed and migrated to other drives in the cluster before the drive is removed from the cluster. This is an asynchronous method. Depending on the total capacity of the drives being removed, it might take several minutes to migrate all of the data. Use the GetAsyncResult method to check the status of the remove operation. When removing multiple drives, use a single RemoveDrives method call rather than multiple individual methods with a single drive each. This reduces the amount of data balancing that must occur to even stabilize the storage load on the cluster. You can also remove drives with a "failed" status using RemoveDrives. When you remove a drive with a "failed" status it is not returned to an "available" or active status. The drive is unavailable for use in the cluster. Use the ListDrives method to obtain the driveIDs for the drives you want to remove. 

Options:
--drives
List of driveIDs to remove from the cluster. 

--forceduringupgrade
If you want to remove a drive during upgrade, this must be set to true. 

---------------------------------------------------------------
#### getconfig ####
Command:

    sfcli Drive getconfig <options>

Description:

GetDriveConfig enables you to display drive information for expected slice and block drive counts as well as the number of slices and block drives that are currently connected to the node. Note: This method is available only through the per-node API endpoint 5.0 or later. 

Options:
---------------------------------------------------------------
#### list ####
Command:

    sfcli Drive list <options>

Description:

ListDrives enables you to retrieve the list of the drives that exist in the cluster's active nodes. This method returns drives that have been added as volume metadata or block drives as well as drives that have not been added and are available. 

Options:
---------------------------------------------------------------
#### gethardwareinfo ####
Command:

    sfcli Drive gethardwareinfo <options>

Description:

GetDriveHardwareInfo returns all the hardware information for the given drive. This generally includes details about manufacturers, vendors, versions, and other associated hardware identification information. 

Options:
--driveid
DriveID for the drive information requested. You can get DriveIDs by using the ListDrives method. 

---------------------------------------------------------------
#### test ####
Command:

    sfcli Drive test <options>

Description:

You can use the TestDrives API method to run a hardware validation on all drives on the node. This method detects hardware failures on the drives (if present) and reports them in the results of the validation tests. You can only use the TestDrives method on nodes that are not "active" in a cluster. Note: This test takes approximately 10 minutes. Note: This method is available only through the per-node API endpoint 5.0 or later. 

Options:
--minutes
Specifies the number of minutes to run the test. 

--force
Required parameter to successfully test the drives on the node. 

---------------------------------------------------------------
#### getstats ####
Command:

    sfcli Drive getstats <options>

Description:

GetDriveStats returns high-level activity measurements for a single drive. Values are cumulative from the addition of the drive to the cluster. Some values are specific to block drives. You might not obtain statistical data for both block and metadata drives when you run this method.  

Options:
--driveid
Specifies the drive for which statistics are gathered. 

---------------------------------------------------------------
#### reset ####
Command:

    sfcli Drive reset <options>

Description:

ResetDrives enables you to proactively initialize drives and remove all data currently residing on a drive. The drive can then be reused in an existing node or used in an upgraded node. This method requires the force parameter to be included in the method call. 

Options:
--drives
List of device names (not driveIDs) to reset. 

--force
Required parameter to successfully reset a drive. 

---------------------------------------------------------------
#### liststats ####
Command:

    sfcli Drive liststats <options>

Description:

ListDriveStats enables you to retrieve high-level activity measurements for multiple drives in the cluster. By default, this method returns statistics for all drives in the cluster, and these measurements are cumulative from the addition of the drive to the cluster. Some values this method returns are specific to block drives, and some are specific to metadata drives. 

Options:
--drives
Optional list of DriveIDs for which to return drive statistics. If you omit this parameter, measurements for all drives are returned. 

---------------------------------------------------------------
#### listhardware ####
Command:

    sfcli Drive listhardware <options>

Description:

ListDriveHardware returns all the drives connected to a node. Use this method on individual nodes to return drive hardware information or use this method on the cluster master node MVIP to see information for all the drives on all nodes. Note: The "securitySupported": true line of the method response does not imply that the drives are capable of encryption; only that the security status can be queried. If you have a node type with a model number ending in "-NE", commands to enable security features on these drives will fail. See the EnableEncryptionAtRest method for more information. 

Options:
--force
To run this command, the force parameter must be set to true. 

---------------------------------------------------------------
#### add ####
Command:

    sfcli Drive add <options>

Description:

AddDrives enables you to add one or more available drives to the cluster, enabling the drives to host a portion of the cluster's data. When you add a node to the cluster or install new drives in an existing node, the new drives are marked as "available" and must be added via AddDrives before they can be utilized. Use the ListDrives method to display drives that are "available" to be added. When you add multiple drives, it is more efficient to add them in a single AddDrives method call rather than multiple individual methods with a single drive each. This reduces the amount of data balancing that must occur to stabilize the storage load on the cluster. When you add a drive, the system automatically determines the "type" of drive it should be. The method is asynchronous and returns immediately. However, it can take some time for the data in the cluster to be rebalanced using the newly added drives. As the new drives are syncing on the system, you can use the ListSyncJobs method to see how the drives are being rebalanced and the progress of adding the new drive. You can also use the GetAsyncResult method to query the method's returned asyncHandle. 

Options:
--drives
Returns information about each drive to be added to the cluster. Possible values are: driveID: The ID of the drive to add. (Integer) type: (Optional) The type of drive to add. Valid values are "slice" or "block". If omitted, the system assigns the correct type. (String) 

--driveid
A unique identifier for this drive. 

--type
block or slice 

--forceduringupgrade
Allows the user to force the addition of drives during an upgrade. 

---------------------------------------------------------------
#### secureerase ####
Command:

    sfcli Drive secureerase <options>

Description:

SecureEraseDrives enables you to remove any residual data from drives that have a status of "available." You might want to use this method when replacing a drive nearing the end of its service life that contained sensitive data. This method uses a Security Erase Unit command to write a predetermined pattern to the drive and resets the encryption key on the drive. This asynchronous method might take up to two minutes to complete. You can use GetAsyncResult to check on the status of the secure erase operation. You can use the ListDrives method to obtain the driveIDs for the drives you want to secure erase. 

Options:
--drives
List of driveIDs to be secure erased. 


VirtualVolume Commands 
---------------------------------------------------------------
#### getfeaturestatus ####
Command:

    sfcli VirtualVolume getfeaturestatus <options>

Description:

GetFeatureStatus enables you to retrieve the status of a cluster feature. 

Options:
--feature
Specifies the feature for which the status is returned. Valid value is: vvols: Retrieve status for the NetApp SolidFire VVols cluster feature. 

---------------------------------------------------------------
#### listbindings ####
Command:

    sfcli VirtualVolume listbindings <options>

Description:

ListVirtualVolumeBindings returns a list of all virtual volumes in the cluster that are bound to protocol endpoints. 

Options:
--virtualvolumebindingids
A list of virtual volume binding IDs for which to retrieve information. If you omit this parameter, the method returns information about all virtual volume bindings. 

---------------------------------------------------------------
#### listhosts ####
Command:

    sfcli VirtualVolume listhosts <options>

Description:

ListVirtualVolumeHosts returns a list of all virtual volume hosts known to the cluster. A virtual volume host is a VMware ESX host that has initiated a session with the VASA API provider. 

Options:
--virtualvolumehostids
A list of virtual volume host IDs for which to retrieve information. If you omit this parameter, the method returns information about all virtual volume hosts. 

---------------------------------------------------------------
#### enablefeature ####
Command:

    sfcli VirtualVolume enablefeature <options>

Description:

You can use EnableFeature to enable cluster features that are disabled by default. 

Options:
--feature
Indicates which feature to enable. Valid value is: vvols: Enable the NetApp SolidFire VVols cluster feature. 

---------------------------------------------------------------
#### listvolumestatsby ####
Command:

    sfcli VirtualVolume listvolumestatsby <options>

Description:

ListVolumeStatsByVirtualVolume enables you to list volume statistics for any volumes in the system that are associated with virtual volumes. Statistics are cumulative from the creation of the volume. 

Options:
--virtualvolumeids
A list of one or more virtual volume IDs for which to retrieve information. If you specify this parameter, the method returns information about only these virtual volumes. 

---------------------------------------------------------------
#### list ####
Command:

    sfcli VirtualVolume list <options>

Description:

ListVirtualVolumes enables you to list the virtual volumes currently in the system. You can use this method to list all virtual volumes, or only list a subset. 

Options:
--details
Specifies the level of detail about each virtual volume that is returned. Possible values are: true: Include more details about each virtual volume in the response. false: Include the standard level of detail about each virtual volume in the response. 

--limit
The maximum number of virtual volumes to list. 

--recursive
Specifies whether to include information about the children of each virtual volume in the response. Possible values are: true: Include information about the children of each virtual volume in the response. false: Do not include information about the children of each virtual volume in the response. 

--startvirtualvolumeid
The ID of the virtual volume at which to begin the list. 

--virtualvolumeids
A list of virtual volume IDs for which to retrieve information. If you specify this parameter, the method returns information about only these virtual volumes. 

---------------------------------------------------------------
#### getcount ####
Command:

    sfcli VirtualVolume getcount <options>

Description:

Enables retrieval of the number of virtual volumes currently in the system. 

Options:
---------------------------------------------------------------
#### listprotocolendpoints ####
Command:

    sfcli VirtualVolume listprotocolendpoints <options>

Description:

ListProtocolEndpoints enables you to retrieve information about all protocol endpoints in the cluster. Protocol endpoints govern access to their associated virtual volume storage containers. 

Options:
--protocolendpointids
A list of protocol endpoint IDs for which to retrieve information. If you omit this parameter, the method returns information about all protocol endpoints. 

---------------------------------------------------------------
#### listtasks ####
Command:

    sfcli VirtualVolume listtasks <options>

Description:

ListVirtualVolumeTasks returns a list of virtual volume tasks in the system. 

Options:
--virtualvolumetaskids
A list of virtual volume task IDs for which to retrieve information. If you omit this parameter, the method returns information about all virtual volume tasks. 


Network Commands 
---------------------------------------------------------------
#### listfibrechannelportinfo ####
Command:

    sfcli Network listfibrechannelportinfo <options>

Description:

ListFibreChannelPortInfo enables you to retrieve information about the Fibre Channel ports on a node.  The API method is intended for use on individual nodes; userid and password authentication is required for access to individual Fibre Channel nodes. 

Options:
---------------------------------------------------------------
#### listiscsisessions ####
Command:

    sfcli Network listiscsisessions <options>

Description:

You can use ListISCSISessions to return iSCSI information for volumes in the cluster. 

Options:
---------------------------------------------------------------
#### listfibrechannelsessions ####
Command:

    sfcli Network listfibrechannelsessions <options>

Description:

ListFibreChannelSessions enables you to retrieve information about the active Fibre Channel sessions on a cluster.  

Options:
---------------------------------------------------------------
#### listnodefibrechannelportinfo ####
Command:

    sfcli Network listnodefibrechannelportinfo <options>

Description:

The ListNodeFibreChannelPortInfo API method enables you to retrieve information about the Fibre Channel ports on a node. The API method is intended for use on individual nodes; userid and password authentication is required for access to individual Fibre Channel nodes. 

Options:
---------------------------------------------------------------
#### listinterfaces ####
Command:

    sfcli Network listinterfaces <options>

Description:

ListNetworkInterfaces enables you to retrieve information about each network interface on a node. The API method is intended for use on individual nodes; userid and password authentication is required for access to individual nodes. 

Options:

Snapshot Commands 
---------------------------------------------------------------
#### rollbacktogroup ####
Command:

    sfcli Snapshot rollbacktogroup <options>

Description:

RollbackToGroupSnapshot enables you to roll back all individual volumes in a snapshot group to each volume's individual snapshot. Note: Rolling back to a group snapshot creates a temporary snapshot of each volume within the group snapshot. Snapshots are allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5. 

Options:
--groupsnapshotid
Specifies the unique ID of the group snapshot. 

--savecurrentstate
Specifies whether to save an active volume image or delete it. Values are: true: The previous active volume image is kept. false: (default) The previous active volume image is deleted. 

--name
Name for the group snapshot of the volume's current state that is created if "saveCurrentState" is set to true. If you do not give a name, the name of the snapshots (group and individual volume) are set to a timestamp of the time that the rollback occurred. 

--attributes
List of name-value pairs in JSON object format. 

---------------------------------------------------------------
#### modify ####
Command:

    sfcli Snapshot modify <options>

Description:

ModifySnapshot enables you to change the attributes currently assigned to a snapshot. You can use this method to enable snapshots created on the Read/Write (source) volume to be remotely replicated to a target SolidFire storage system. 

Options:
--snapshotid
Specifies the ID of the snapshot. 

--expirationtime
Sets the time when the snapshot should be removed. 

--enableremotereplication
Replicates the snapshot created to a remote cluster. Possible values are: true: The snapshot is replicated to remote storage. false: Default. The snapshot is not replicated. 

---------------------------------------------------------------
#### rollbackto ####
Command:

    sfcli Snapshot rollbackto <options>

Description:

RollbackToSnapshot enables you to make an existing snapshot of the "active" volume image. This method creates a new snapshot from an existing snapshot. The new snapshot becomes "active" and the existing snapshot is preserved until you delete it. The previously "active" snapshot is deleted unless you set the parameter saveCurrentState to true. Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5. 

Options:
--volumeid
VolumeID for the volume. 

--snapshotid
The ID of a previously created snapshot on the given volume. 

--savecurrentstate
Specifies whether to save an active volume image or delete it. Values are: true: The previous active volume image is kept. false: (default) The previous active volume image is deleted. 

--name
Name for the snapshot. If unspecified, the name of the snapshot being rolled back to is used with "- copy" appended to the end of the name. 

--attributes
List of name-value pairs in JSON object format. 

---------------------------------------------------------------
#### delete ####
Command:

    sfcli Snapshot delete <options>

Description:

DeleteSnapshot enables you to delete a snapshot. A snapshot that is currently the "active" snapshot cannot be deleted. You must rollback and make another snapshot "active" before the current snapshot can be deleted. For more details on rolling back snapshots, see RollbackToSnapshot. 

Options:
--snapshotid
The ID of the snapshot to be deleted. 

---------------------------------------------------------------
#### create ####
Command:

    sfcli Snapshot create <options>

Description:

CreateSnapshot enables you to create a point-in-time copy of a volume. You can create a snapshot from any volume or from an existing snapshot. If you do not provide a SnapshotID with this API method, a snapshot is created from the volume's active branch. If the volume from which the snapshot is created is being replicated to a remote cluster, the snapshot can also be replicated to the same target. Use the enableRemoteReplication parameter to enable snapshot replication. Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5. 

Options:
--volumeid
Specifies the unique ID of the volume image from which to copy. 

--snapshotid
Specifies the unique ID of a snapshot from which the new snapshot is made. The snapshotID passed must be a snapshot on the given volume. 

--name
Specifies a name for the snapshot. If unspecified, the date and time the snapshot was taken is used. 

--enableremotereplication
Replicates the snapshot created to a remote cluster. Possible values are: true: The snapshot is replicated to remote storage. false: Default. The snapshot is not replicated. 

--retention
Specifies the amount of time for which the snapshot is retained. The format is HH:mm:ss. 

--attributes
List of name-value pairs in JSON object format. 

---------------------------------------------------------------
#### creategroup ####
Command:

    sfcli Snapshot creategroup <options>

Description:

CreateGroupSnapshot enables you to create a point-in-time copy of a group of volumes. You can use this snapshot later as a backup or rollback to ensure the data on the group of volumes is consistent for the point in time that you created the snapshot. Note: Creating a group snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5. 

Options:
--volumes
Unique ID of the volume image from which to copy. 

--name
Name for the group snapshot. If unspecified, the date and time the group snapshot was taken is used. 

--enableremotereplication
Replicates the snapshot created to remote storage. Possible values are: true: The snapshot is replicated to remote storage. false: Default. The snapshot is not replicated. 

--retention
Specifies the amount of time for which the snapshots are retained. The format is HH:mm:ss. 

--attributes
List of name-value pairs in JSON object format. 

---------------------------------------------------------------
#### modifygroup ####
Command:

    sfcli Snapshot modifygroup <options>

Description:

ModifyGroupSnapshot enables you to change the attributes of a group of snapshots. You can also use this method to enable snapshots created on the Read/Write (source) volume to be remotely replicated to a target SolidFire storage system. 

Options:
--groupsnapshotid
Specifies the ID of the group of snapshots. 

--expirationtime
Sets the time when the snapshot should be removed. If unspecified, the current time is used. 

--enableremotereplication
Replicates the snapshot created to a remote cluster. Possible values are: true: The snapshot is replicated to remote storage. false: Default. The snapshot is not replicated. 

---------------------------------------------------------------
#### list ####
Command:

    sfcli Snapshot list <options>

Description:

ListSnapshots enables you to return the attributes of each snapshot taken on the volume. Information about snapshots that reside on the target cluster is displayed on the source cluster when this method is called from the source cluster. 

Options:
--volumeid
Retrieves snapshots for a volume. If volumeID is not provided, all snapshots for all volumes are returned. 

--snapshotid
Retrieves information for a specific snapshot ID. 

---------------------------------------------------------------
#### listgroup ####
Command:

    sfcli Snapshot listgroup <options>

Description:

ListGroupSnapshots enables you to get information about all group snapshots that have been created. 

Options:
--volumes
An array of unique volume IDs to query. If you do not specify this parameter, all group snapshots on the cluster are included. 

--groupsnapshotid
Retrieves information for a specific group snapshot ID. 

---------------------------------------------------------------
#### deletegroup ####
Command:

    sfcli Snapshot deletegroup <options>

Description:

DeleteGroupSnapshot enables you to delete a group snapshot. You can use the saveMembers parameter to preserve all the snapshots that were made for the volumes in the group, but the group association is removed. 

Options:
--groupsnapshotid
Specifies the unique ID of the group snapshot. 

--savemembers
Specifies whether to preserve snapshots or delete them. Valid values are: true: Snapshots are preserved, but group association is removed. false: The group and snapshots are deleted. 


Cluster Commands 
---------------------------------------------------------------
#### getcompletestats ####
Command:

    sfcli Cluster getcompletestats <options>

Description:

NetApp engineering uses the GetCompleteStats API method to troubleshoot new features. The data returned from GetCompleteStats is not documented, changes frequently, and is not guaranteed to be accurate. NetApp does not recommend using GetCompleteStats for collecting performance data or any other management integration with a SolidFire cluster. 

Options:
---------------------------------------------------------------
#### create ####
Command:

    sfcli Cluster create <options>

Description:

The CreateCluster method enables you to initialize the node in a cluster that has ownership of the "mvip" and "svip" addresses. Each new cluster is initialized using the management IP (MIP) of the first node in the cluster. This method also automatically adds all the nodes being configured into the cluster. You only need to use this method once each time a new cluster is initialized. Note: You need to log in to the node that is used as the master node for the cluster. After you log in, run the GetBootstrapConfig method on the node to get the IP addresses for the rest of the nodes that you want to include in the cluster. Then, run the CreateCluster method. 

Options:
--mvip
Floating (virtual) IP address for the cluster on the management network. 

--svip
Floating (virtual) IP address for the cluster on the storage (iSCSI) network. 

--repcount
Number of replicas of each piece of data to store in the cluster. Valid value is "2". 

--username
Username for the cluster admin. 

--password
Initial password for the cluster admin account. 

--nodes
CIP/SIP addresses of the initial set of nodes making up the cluster. This node's IP must be in the list. 

--accepteula
Required to indicate your acceptance of the End User License Agreement when creating this cluster. To accept the EULA, set this parameter to true. 

--attributes
List of name-value pairs in JSON object format. 

---------------------------------------------------------------
#### getfullthreshold ####
Command:

    sfcli Cluster getfullthreshold <options>

Description:

You can use GetClusterFullThreshold to view the stages set for cluster fullness levels. This method returns all fullness metrics for the cluster. Note: When a cluster reaches the Error stage of block cluster fullness, the maximum IOPS on all volumes are reduced linearly to the volume's minimum IOPS as the cluster approaches the Critical stage. This helps prevent the cluster from reaching the Critical stage of block cluster fullness. 

Options:
---------------------------------------------------------------
#### enableencryptionatrest ####
Command:

    sfcli Cluster enableencryptionatrest <options>

Description:

You can use the EnableEncryptionAtRest method to enable the Advanced Encryption Standard (AES) 256-bit encryption at rest on the cluster, so that the cluster can manage the encryption key used for the drives on each node. This feature is not enabled by default. When you enable Encryption at Rest, the cluster automatically manages encryption keys internally for the drives on each node in the cluster. Nodes do not store the keys to unlock drives and the keys are never passed over the network. Two nodes participating in a cluster are required to access the key to disable encryption on a drive. The encryption management does not affect performance or efficiency on the cluster. If an encryption-enabled drive or node is removed from the cluster with the API, Encryption at Rest is disabled and the data is not secure erased. Data can be secure erased using the SecureEraseDrives API method. Note: If you have a node type with a model number ending in "-NE", the EnableEncryptionAtRest method call fails with a response of "Encryption not allowed. Cluster detected non-encryptable node". You should only enable or disable encryption when the cluster is running and in a healthy state. You can enable or disable encryption at your discretion and as often as you need. Note: This process is asynchronous and returns a response before encryption is enabled. You can use the GetClusterInfo method to poll the system to see when the process has completed. 

Options:
---------------------------------------------------------------
#### getinfo ####
Command:

    sfcli Cluster getinfo <options>

Description:

GetClusterInfo enables you to return configuration information about the cluster. 

Options:
---------------------------------------------------------------
#### setconfig ####
Command:

    sfcli Cluster setconfig <options>

Description:

The SetClusterConfig API method enables you to set the configuration this node uses to communicate with the cluster it is associated with. To see the states in which these objects can be modified, see Cluster Object Attributes. To display the current cluster interface settings for a node, run the GetClusterConfig API method. Note: This method is available only through the per-node API endpoint 5.0 or later. 

Options:
--clusterconfig
Network interface used for cluster communication. 

--clusterconfig
Unique cluster name. 

--clusterconfig
Nodes that are participating in the cluster. 

--clusterconfig
Network interface used for node management. 

--clusterconfig
Unique cluster name. 

--clusterconfig
 

--clusterconfig
 

--clusterconfig
Identifies the role of the node 

--clusterconfig
Network interface used for storage. 

--clusterconfig
 

--clusterconfig
 

--clusterconfig
 

--clusterconfig
 

--cipi
Network interface used for cluster communication. 

--clustercluster
Unique cluster name. 

--ensemble
Nodes that are participating in the cluster. 

--mipi
Network interface used for node management. 

--name
Unique cluster name. 

--nodeid
 

--pendingnodeid
 

--role
Identifies the role of the node 

--sipi
Network interface used for storage. 

--state
 

--encryptioncapable
 

--haslocaladmin
 

--version
 

---------------------------------------------------------------
#### getversioninfo ####
Command:

    sfcli Cluster getversioninfo <options>

Description:

GetClusterVersionInfo enables you to retrieve information about the Element software version running on each node in the cluster. This method also returns information about nodes that are currently in the process of upgrading software. 

Options:
---------------------------------------------------------------
#### listevents ####
Command:

    sfcli Cluster listevents <options>

Description:

ListEvents returns events detected on the cluster, sorted from oldest to newest. 

Options:
--maxevents
Specifies the maximum number of events to return. 

--starteventid
Identifies the beginning of a range of events to return. 

--endeventid
Identifies the end of a range of events to return. 

---------------------------------------------------------------
#### modifyfullthreshold ####
Command:

    sfcli Cluster modifyfullthreshold <options>

Description:

You can use ModifyClusterFullThreshold to change the level at which the system generates an event when the storage cluster approaches a certain capacity utilization. You can use the threshold setting to indicate the acceptable amount of utilized block storage before the system generates a warning. For example, if you want to be alerted when the system reaches 3% below the "Error" level block storage utilization, enter a value of "3" for the stage3BlockThresholdPercent parameter. If this level is reached, the system sends an alert to the Event Log in the Cluster Management Console. 

Options:
--stage2awarethreshold
The number of nodes of capacity remaining in the cluster before the system triggers a capacity notification. 

--stage3blockthresholdpercent
The percentage of block storage utilization below the "Error" threshold that causes the system to trigger a cluster "Warning" alert. 

--maxmetadataoverprovisionfactor
A value representative of the number of times metadata space can be overprovisioned relative to the amount of space available. For example, if there was enough metadata space to store 100 TiB of volumes and this number was set to 5, then 500 TiB worth of volumes can be created. 

---------------------------------------------------------------
#### deleteallsupportbundles ####
Command:

    sfcli Cluster deleteallsupportbundles <options>

Description:

DeleteAllSupportBundles enables you to delete all support bundles generated with the CreateSupportBundle API method. 

Options:
---------------------------------------------------------------
#### clearfaults ####
Command:

    sfcli Cluster clearfaults <options>

Description:

You can use the ClearClusterFaults method to clear information about both current and previously detected faults. Both resolved and unresolved faults can be cleared. 

Options:
--faulttypes
Determines the types of faults cleared. Possible values are: current: Faults that are currently detected and have not been resolved. resolved: (Default) Faults that were previously detected and resolved. all: Both current and resolved faults are cleared. The fault status can be determined by the resolved field of the fault object. 

---------------------------------------------------------------
#### getapi ####
Command:

    sfcli Cluster getapi <options>

Description:

You can use the GetAPI method to return a list of all the API methods and supported API endpoints that can be used in the system. 

Options:
---------------------------------------------------------------
#### getstate ####
Command:

    sfcli Cluster getstate <options>

Description:

The GetClusterState API method enables you to indicate if a node is part of a cluster or not. The three states are: Available: Node has not been configured with a cluster name. Pending: Node is pending for a specific named cluster and can be added. Active: Node is an active member of a cluster and may not be added to another cluster. Note: This method is available only through the per-node API endpoint 5.0 or later. 

Options:
--force
To run this command, the force parameter must be set to true. 

---------------------------------------------------------------
#### getrawstats ####
Command:

    sfcli Cluster getrawstats <options>

Description:

NetApp engineering uses the GetRawStats API method to troubleshoot new features. The data returned from GetRawStats is not documented, changes frequently, and is not guaranteed to be accurate. NetApp does not recommend using GetCompleteStats for collecting performance data or any other management integration with a SolidFire cluster. 

Options:
---------------------------------------------------------------
#### getcapacity ####
Command:

    sfcli Cluster getcapacity <options>

Description:

You can use the GetClusterCapacity method to return the high-level capacity measurements for an entire cluster. You can use the fields returned from this method to calculate the efficiency rates that are displayed in the Element OS Web UI. You can use the following calculations in scripts to return the efficiency rates for thin provisioning, deduplication, compression, and overall efficiency. 

Options:
---------------------------------------------------------------
#### setntpinfo ####
Command:

    sfcli Cluster setntpinfo <options>

Description:

SetNtpInfo enables you to configure NTP on cluster nodes. The values you set with this interface apply to all nodes in the cluster. If an NTP broadcast server periodically broadcasts time information on your network, you can optionally configure nodes as broadcast clients. Note: NetApp recommends using NTP servers that are internal to your network, rather than the installation defaults. 

Options:
--servers
List of NTP servers to add to each nodes NTP configuration. 

--broadcastclient
Enables every node in the cluster as a broadcast client. 

---------------------------------------------------------------
#### getntpinfo ####
Command:

    sfcli Cluster getntpinfo <options>

Description:

GetNtpInfo enables you to return the current network time protocol (NTP) configuration information. 

Options:
---------------------------------------------------------------
#### disableencryptionatrest ####
Command:

    sfcli Cluster disableencryptionatrest <options>

Description:

The DisableEncryptionAtRest method enables you to remove the encryption that was previously applied to the cluster using the EnableEncryptionAtRest method. This disable method is asynchronous and returns a response before encryption is disabled. You can use the GetClusterInfo method to poll the system to see when the process has completed. 

Options:
---------------------------------------------------------------
#### getmasternodeid ####
Command:

    sfcli Cluster getmasternodeid <options>

Description:

GetClusterMasterNodeID enables you to retrieve the ID of the node that can perform cluster-wide administration tasks and holds the storage virtual IP address (SVIP) and management virtual IP address (MVIP). 

Options:
---------------------------------------------------------------
#### listfaults ####
Command:

    sfcli Cluster listfaults <options>

Description:

ListClusterFaults enables you to retrieve information about any faults detected on the cluster. With this method, you can retrieve both current faults as well as faults that have been resolved. The system caches faults every 30 seconds. 

Options:
--bestpractices
Specifies whether to include faults triggered by suboptimal system configuration. Possible values are: true false 

--faulttypes
Determines the types of faults returned. Possible values are: current: List active, unresolved faults. resolved: List faults that were previously detected and resolved. all: (Default) List both current and resolved faults. You can see the fault status in the resolved field of the Cluster Fault object. 

---------------------------------------------------------------
#### getconfig ####
Command:

    sfcli Cluster getconfig <options>

Description:

The GetClusterConfig API method enables you to return information about the cluster configuration this node uses to communicate with the cluster that it is a part of. 

Options:
---------------------------------------------------------------
#### getsystemstatus ####
Command:

    sfcli Cluster getsystemstatus <options>

Description:

GetSystemStatus enables you to return whether a reboot ir required or not. 

Options:
---------------------------------------------------------------
#### listsyncjobs ####
Command:

    sfcli Cluster listsyncjobs <options>

Description:

ListSyncJobs enables you to return information about synchronization jobs that are running on a SolidFire cluster. The type of synchronization jobs that are returned with this method are slice, clone, and remote. 

Options:
---------------------------------------------------------------
#### getlimits ####
Command:

    sfcli Cluster getlimits <options>

Description:

GetLimits enables you to retrieve the limit values set by the API. These values might change between releases of Element OS, but do not change without an update to the system. Knowing the limit values set by the API can be useful when writing API scripts for user-facing tools. Note: The GetLimits method returns the limits for the current software version regardless of the API endpoint version used to pass the method. 

Options:
---------------------------------------------------------------
#### getstats ####
Command:

    sfcli Cluster getstats <options>

Description:

GetClusterStats enables you to retrieve high-level activity measurements for the cluster. Values returned are cumulative from the creation of the cluster. 

Options:
---------------------------------------------------------------
#### createsupportbundle ####
Command:

    sfcli Cluster createsupportbundle <options>

Description:

CreateSupportBundle enables you to create a support bundle file under the node's directory. After creation, the bundle is stored on the node as a tar.gz file. 

Options:
--bundlename
The unique name for the support bundle. If no name is provided, "supportbundle" and the node name are used as the filename. 

--extraargs
Passed to the sf_make_support_bundle script. You should use this parameter only at the request of NetApp SolidFire Support. 

--timeoutsec
The number of seconds to allow the support bundle script to run before stopping. The default value is 1500 seconds. 


Test Commands 
---------------------------------------------------------------
#### listutilities ####
Command:

    sfcli Test listutilities <options>

Description:

You can use the ListUtilities API method to return the operations that are available to run on a node.  Note: This method is available only through the per-node API endpoint 5.0 or later. 

Options:
---------------------------------------------------------------
#### connectensemble ####
Command:

    sfcli Test connectensemble <options>

Description:

The TestConnectEnsemble API method enables you to verify connectivity with a specified database ensemble. By default, it uses the ensemble for the cluster that the node is associated with. Alternatively, you can provide a different ensemble to test connectivity with. Note: This method is available only through the per-node API endpoint 5.0 or later. 

Options:
--ensemble
Uses a comma-separated list of ensemble node cluster IP addresses to test connectivity. This parameter is optional. 

---------------------------------------------------------------
#### ping ####
Command:

    sfcli Test ping <options>

Description:

You can use the TestPing API method to validate the connection to all the nodes in a cluster on both 1G and 10G interfaces by using ICMP packets. The test uses the appropriate MTU sizes for each packet based on the MTU settings in the network configuration. Note: This method is available only through the per-node API endpoint 5.0 or later. 

Options:
--attempts
Specifies the number of times the system should repeat the test ping. The default value is 5. 

--hosts
Specifies a comma-separated list of addresses or hostnames of devices to ping. 

--totaltimeoutsec
Specifies the length of time the ping should wait for a system response before issuing the next ping attempt or ending the process. 

--packetsize
Specifies the number of bytes to send in the ICMP packet that is sent to each IP. The number must be less than the maximum MTU specified in the network configuration. 

--pingtimeoutmsec
Specifies the number of milliseconds to wait for each individual ping response. The default value is 500 ms. 

--prohibitfragmentation
Specifies that the Do not Fragment (DF) flag is enabled for the ICMP packets. 

---------------------------------------------------------------
#### list ####
Command:

    sfcli Test list <options>

Description:

You can use the ListTests API method to return the tests that are available to run on a node. Note: This method is available only through the per-node API endpoint 5.0 or later. 

Options:
---------------------------------------------------------------
#### connectmvip ####
Command:

    sfcli Test connectmvip <options>

Description:

The TestConnectMvip API method enables you to test the management connection to the cluster. The test pings the MVIP and executes a simple API method to verify connectivity. Note: This method is available only through the per-node API endpoint 5.0 or later. 

Options:
--mvip
If specified, tests the management connection of a different MVIP. You do not need to use this value when testing the connection to the target cluster. This parameter is optional. 

---------------------------------------------------------------
#### connectsvip ####
Command:

    sfcli Test connectsvip <options>

Description:

The TestConnectSvip API method enables you to test the storage connection to the cluster. The test pings the SVIP using ICMP packets, and when successful, connects as an iSCSI initiator. Note: This method is available only through the per-node API endpoint 5.0 or later. 

Options:
--svip
If specified, tests the storage connection of a different SVIP. You do not need to use this value when testing the connection to the target cluster. This parameter is optional. 


VirtualNetwork Commands 
---------------------------------------------------------------
#### modify ####
Command:

    sfcli VirtualNetwork modify <options>

Description:

You can use ModifyVirtualNetwork to change the attributes of an existing virtual network. This method enables you to add or remove address blocks, change the netmask, or modify the name or description of the virtual network. You can also use it to enable or disable namespaces, as well as add or remove a gateway if namespaces are enabled on the virtual network. Note: This method requires either the VirtualNetworkID or the VirtualNetworkTag as a parameter, but not both. Caution: Enabling or disabling the Routable Storage VLANs functionality for an existing virtual network by changing the "namespace" parameter disrupts any traffic handled by the virtual network. NetApp strongly recommends changing the "namespace" parameter only during a scheduled maintenance window. 

Options:
--virtualnetworkid
The unique identifier of the virtual network to modify. This is the virtual network ID assigned by the cluster.  Note: This parameter is optional but either virtualNetworkID or virtualNetworkTag must be specified with this API method. 

--virtualnetworktag
The network tag that identifies the virtual network to modify. Note: This parameter is optional but either virtualNetworkID or virtualNetworkTag must be specified with this API method. 

--name
The new name for the virtual network. 

--addressblocks
The new addressBlock to set for this virtual network. This might contain new address blocks to add to the existing object or omit unused address blocks that need to be removed. Alternatively, you can extend or reduce the size of existing address blocks. You can only increase the size of the starting addressBlocks for a virtual network object; you can never decrease it. Attributes for this parameter are: start: The start of the IP address range. (String) size: The number of IP addresses to include in the block. (Integer) 

--netmask
New network mask for this virtual network. 

--svip
The storage virtual IP address for this virtual network. The svip for a virtual network cannot be changed. You must create a new virtual network to use a different svip address. 

--gateway
The IP address of a gateway of the virtual network. This parameter is only valid if the "namespace" parameter is set to true. 

--namespace
When set to true, enables Routable Storage VLANs functionality by recreating the virtual network and configuring a namespace to contain it. When set to false, disables the VRF functionality for the virtual network. Changing this value disrupts traffic running through this virtual network. 

--attributes
A new list of name-value pairs in JSON object format. 

---------------------------------------------------------------
#### list ####
Command:

    sfcli VirtualNetwork list <options>

Description:

ListVirtualNetworks enables you to list all configured virtual networks for the cluster. You can use this method to verify the virtual network settings in the cluster. There are no required parameters for this method. However, to filter the results, you can pass one or more VirtualNetworkID or VirtualNetworkTag values. 

Options:
--virtualnetworkid
Network ID to filter the list for a single virtual network. 

--virtualnetworktag
Network tag to filter the list for a single virtual network. 

--virtualnetworkids
Network IDs to include in the list. 

--virtualnetworktags
Network tag to include in the list. 

---------------------------------------------------------------
#### remove ####
Command:

    sfcli VirtualNetwork remove <options>

Description:

RemoveVirtualNetwork enables you to remove a previously added virtual network. Note: This method requires either the virtualNetworkID or the virtualNetworkTag as a parameter, but not both. 

Options:
--virtualnetworkid
Network ID that identifies the virtual network to remove. 

--virtualnetworktag
Network tag that identifies the virtual network to remove. 

---------------------------------------------------------------
#### add ####
Command:

    sfcli VirtualNetwork add <options>

Description:

You can use the AddVirtualNetwork method to add a new virtual network to a cluster configuration. When you add a virtual network, an interface for each node is created and each interface will require a virtual network IP address. The number of IP addresses you specify as a parameter for this API method must be equal to or greater than the number of nodes in the cluster. The system bulk provisions virtual network addresses and assigns them to individual nodes automatically. You do not need to assign virtual network addresses to nodes manually. Note: You can use AddVirtualNetwork only to create a new virtual network. If you want to make changes to an existing virtual network, use ModifyVirtualNetwork. Note: Virtual network parameters must be unique to each virtual network when setting the namespace parameter to false. 

Options:
--virtualnetworktag
A unique virtual network (VLAN) tag. Supported values are 1 through 4094.The number zero (0) is not supported. 

--name
A user-defined name for the new virtual network. 

--addressblocks
Unique range of IP addresses to include in the virtual network. Attributes for this parameter are: start: The start of the IP address range. (String) size: The number of IP addresses to include in the block. (Integer) 

--netmask
Unique network mask for the virtual network being created. 

--svip
Unique storage IP address for the virtual network being created. 

--start
Start of the IP address range. 

--size
Number of IP addresses to include in the block. 

--available
Nuber of available blocks 

--gateway
The IP address of a gateway of the virtual network. This parameter is only valid if the "namespace" parameter is set to true. 

--namespace
When set to true, enables the Routable Storage VLANs functionality by creating and configuring a namespace and the virtual network contained by it. 

--attributes
List of name-value pairs in JSON object format. 


Snmp Commands 
---------------------------------------------------------------
#### enable ####
Command:

    sfcli Snmp enable <options>

Description:

EnableSnmp enables you to enable SNMP on cluster nodes. When you enable SNMP, the action applies to all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to EnableSnmp. 

Options:
--snmpv3enabled
If set to "true", then SNMP v3 is enabled on each node in the cluster. If set to "false", then SNMP v2 is enabled. 

---------------------------------------------------------------
#### setacl ####
Command:

    sfcli Snmp setacl <options>

Description:

SetSnmpACL enables you to configure SNMP access permissions on the cluster nodes. The values you set with this interface apply to all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to SetSnmpACL. Also note that the values set with this interface replace all network or usmUsers values set with the older SetSnmpInfo. 

Options:
--networks
List of networks and what type of access they have to the SNMP servers running on the cluster nodes. See SNMP Network Object for possible "networks" values. This parameter is required if SNMP v3 is disabled. 

--usmusers
List of users and the type of access they have to the SNMP servers running on the cluster nodes. 

--accessnetworks
ro: read-only access.* rw: for read-write access. rosys: for read-only access to a restricted set of system information *SolidFire recommends that all networks other than the default "localhost" be set to "ro" access, because all SolidFire MIB objects are read-only. 

--cidr
A CIDR network mask. This network mask must be an integer greater than or equal to 0, and less than or equal to 32. It must also not be equal to 31. 

--community
SNMP community string. 

--network
This parameter ainteger with the cidr variable is used to control which network the access and community string apply to. The special value of "default" is used to specify an entry that applies to all networks. The cidr mask is ignored when network value is either a host name or default. 

--accessusmusers
rouser: read-only access.* rwuser: for read-write access. rosys: for read-only access to a restricted set of system information *SolidFire recommends that all USM users be set to "rouser" access, because all SolidFire MIB objects are read-only. 

--name
The name of the user. Must contain at least one character, but no more than 32 characters. Blank spaces are not allowed. 

--password
The password of the user. Must be between 8 and 255 characters integer (inclusive). Blank spaces are not allowed. Required if "secLevel" is "auth" or "priv." 

--passphrase
The passphrase of the user. Must be between 8 and 255 characters integer (inclusive). Blank spaces are not allowed. Required if "secLevel" is "priv." 

--seclevel
noauth: No password or passphrase is required. auth: A password is required for user access. priv: A password and passphrase is required for user access. 

---------------------------------------------------------------
#### disable ####
Command:

    sfcli Snmp disable <options>

Description:

You can use DisableSnmp to disable SNMP on the cluster nodes. 

Options:
---------------------------------------------------------------
#### getstate ####
Command:

    sfcli Snmp getstate <options>

Description:

You can use GetSnmpState to return the current state of the SNMP feature. 

Options:
---------------------------------------------------------------
#### getinfo ####
Command:

    sfcli Snmp getinfo <options>

Description:

GetSnmpInfo enables you to retrieve the current simple network management protocol (SNMP) configuration information. Note: GetSnmpInfo is available for Element OS 8 and prior releases. It is deprecated for versions later than Element OS 8. NetApp recommends that you migrate to the GetSnmpState and SetSnmpACL methods. See details in the Element API Reference Guide for their descriptions and usage. 

Options:
---------------------------------------------------------------
#### gettrapinfo ####
Command:

    sfcli Snmp gettrapinfo <options>

Description:

You can use GetSnmpTrapInfo to return current SNMP trap configuration information. 

Options:
---------------------------------------------------------------
#### sendtesttraps ####
Command:

    sfcli Snmp sendtesttraps <options>

Description:

SnmpSendTestTraps enables you to test SNMP functionality for a cluster. This method instructs the cluster to send test SNMP traps to the currently configured SNMP manager. 

Options:
---------------------------------------------------------------
#### settrapinfo ####
Command:

    sfcli Snmp settrapinfo <options>

Description:

You can use SetSnmpTrapInfo to enable and disable the generation of cluster SNMP notifications (traps) and to specify the set of network host computers that receive the notifications. The values you pass with each SetSnmpTrapInfo method call replace all values set in any previous call to SetSnmpTrapInfo. 

Options:
--traprecipients
List of hosts that are to receive the traps generated by the Cluster Master. At least one object is required if any one of the trap types is enabled. 

--clusterfaulttrapsenabled
If the value is set to true, a corresponding solidFireClusterFaultNotification is sent to the configured list of trap recipients when a cluster fault is logged. The default value is false. 

--clusterfaultresolvedtrapsenabled
If the value is set to true, a corresponding solidFireClusterFaultResolvedNotification is sent to the configured list of trap recipients when a cluster fault is resolved. The default value is false. 

--clustereventtrapsenabled
If the value is set to true, a corresponding solidFireClusterEventNotification is sent to the configured list of trap recipients when a cluster event is logged. The default value is false. 

--host
The IP address or host name of the target network management station. 

--community
SNMP community string. 

--port
The UDP port number on the host where the trap is to be sent. Valid range is 1 - 65535. 0 (zero) is not a valid port number. Default is 162. 

---------------------------------------------------------------
#### getacl ####
Command:

    sfcli Snmp getacl <options>

Description:

GetSnmpACL enables you to return the current SNMP access permissions on the cluster nodes. 

Options:
---------------------------------------------------------------
#### setinfo ####
Command:

    sfcli Snmp setinfo <options>

Description:

SetSnmpInfo enables you to configure SNMP version 2 and version 3 on cluster nodes. The values you set with this interface apply to all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to SetSnmpInfo. Note: SetSnmpInfo is deprecated. Use the EnableSnmp and SetSnmpACL methods instead. 

Options:
--networks
List of networks and what type of access they have to the SNMP servers running on the cluster nodes. See the SNMP Network Object for possible "networks" values. This parameter is required only for SNMP v2. 

--enabled
If set to true, SNMP is enabled on each node in the cluster. 

--snmpv3enabled
If set to true, SNMP v3 is enabled on each node in the cluster. 

--usmusers
If SNMP v3 is enabled, this value must be passed in place of the networks parameter. This parameter is required only for SNMP v3. 


Async Commands 
---------------------------------------------------------------
#### getresult ####
Command:

    sfcli Async getresult <options>

Description:

You can use GetAsyncResult to retrieve the result of asynchronous method calls. Some method calls require some time to run, and might not be finished when the system sends the initial response. To obtain the status or result of the method call, use GetAsyncResult to poll the asyncHandle value returned by the method. GetAsyncResult returns the overall status of the operation (in progress, completed, or error) in a standard fashion, but the actual data returned for the operation depends on the original method call and the return data is documented with each method. 

Options:
--asynchandle
A value that was returned from the original asynchronous method call. 

--keepresult
If true, GetAsyncResult does not remove the asynchronous result upon returning it, enabling future queries to that asyncHandle. 

---------------------------------------------------------------
#### listresults ####
Command:

    sfcli Async listresults <options>

Description:

You can use ListAsyncResults to list the results of all currently running and completed asynchronous methods on the system. Querying asynchronous results with ListAsyncResults does not cause completed asyncHandles to expire; you can use GetAsyncResult to query any of the asyncHandles returned by ListAsyncResults. 

Options:
--asyncresulttypes
An optional list of types of results. You can use this list to restrict the results to only these types of operations. Possible values are: BulkVolume: Copy operations between volumes, such as backups or restores. Clone: Volume cloning operations. DriveRemoval: Operations involving the system copying data from a drive in preparation to remove it from the cluster. RtfiPendingNode: Operations involving the system installing compatible software on a node before adding it to the cluster 


Hardware Commands 
---------------------------------------------------------------
#### getclusterinfo ####
Command:

    sfcli Hardware getclusterinfo <options>

Description:

You can use the GetClusterHardwareInfo method to retrieve the hardware status and information for all Fibre Channel nodes, iSCSI nodes and drives in the cluster. This generally includes details about manufacturers, vendors, versions, and other associated hardware identification information. 

Options:
--type
Includes only a certain type of hardware information in the response. Possible values are: drives: List only drive information in the response. nodes: List only node information in the response. all: Include both drive and node information in the response. If this parameter is omitted, a type of "all" is assumed. 

---------------------------------------------------------------
#### getnvraminfo ####
Command:

    sfcli Hardware getnvraminfo <options>

Description:

GetNvramInfo enables you to retrieve information from each node about the NVRAM card. 

Options:
--force
Required parameter to successfully run on all nodes in the cluster. 

---------------------------------------------------------------
#### getnodeinfo ####
Command:

    sfcli Hardware getnodeinfo <options>

Description:

GetNodeHardwareInfo enables you to return all the hardware information and status for the node specified. This generally includes details about manufacturers, vendors, versions, and other associated hardware identification information. 

Options:
--nodeid
The ID of the node for which hardware information is being requested. Information about a Fibre Channel node is returned if a Fibre Channel node is specified. 

---------------------------------------------------------------
#### getconfig ####
Command:

    sfcli Hardware getconfig <options>

Description:

GetHardwareConfig enables you to display the hardware configuration information for a node. Note: This method is available only through the per-node API endpoint 5.0 or later. 

Options:
---------------------------------------------------------------
#### getinfo ####
Command:

    sfcli Hardware getinfo <options>

Description:

The GetHardwareInfo API method enables you to return hardware information and status for a single node. This generally includes details about manufacturers, vendors, versions, drives, and other associated hardware identification information. 

Options:
