import click

from solidfire.cli import utils as cli_utils
from solidfire.cli.cli import pass_context
from solidfire.solidfire_element_api import SolidFireRequestException
from solidfire import utils


@click.group()
@pass_context
def cli(ctx):
    """Volume methods."""
    ctx.sfapi = ctx.client


def _list_volumes(ctx, accounts=None, deleted=True):
    volumes = []
    if ctx.sfapi_endpoint_version >= 8:
        volumes = ctx.sfapi.list_volumes(accounts=accounts)
    else:
        active_vols = ctx.sfapi.list_active_volumes()
        deleted_vols = ctx.sfapi.list_deleted_volumes()
        if accounts:
            active_vols = [vol for vol in active_vols if
                           vol['accountID'] in accounts]
            deleted_vols = [vol for vol in deleted_vols if
                            vol['accountID'] in accounts]
        volumes.extend(active_vols)
        if deleted:
            volumes.extend(deleted_vols)
    return sorted(volumes, key=lambda k: k['volumeID'])


def _get_volume(ctx, volume_id):
    volumes = _list_volumes(ctx)
    vols = [vol for vol in volumes if vol['volumeID'] == int(volume_id)]
    vol = vols[0]

    # qos = vol['qos']
    # TODO(jdg): Add an option for curve, and figure
    # out a way to display it.  For now just remove it
    # qos.pop('curve', None)
    return vol


@cli.command('list', short_help='List volumes.')
@click.option('--deleted/--no-deleted',
              default=True,
              help='Include deleted (non-purged) volumes.')
@click.option('--accounts',
              default=None,
              help='List only for the specified list of account ID\'s.')
@pass_context
def list(ctx, accounts=None, deleted=True):
    """List Volumes."""
    volumes = _list_volumes(ctx, accounts, deleted)
    key_list = ['volumeID', 'iqn', 'enable512e',
                'qos', 'totalSize']
    cli_utils.print_list(volumes, key_list)


@cli.command('delete', short_help='Deletes a volume(s).')
@click.argument('volumes',
                nargs=-1)
@click.option('--purge/--no-purge',
              default=False,
              help='Purge volume(s) on delete.')
@pass_context
def delete(ctx, volumes, purge):
    """Delete the specified volumeID(s)."""
    for vid in volumes:
        try:
            ctx.sfapi.delete_volume(vid)
        except SolidFireRequestException as ex:
            ctx.log(ex.msg[1]['error']['message'])
            pass
    if purge:
        for vid in volumes:
            try:
                ctx.sfapi.purge_deleted_volume(vid)
            except SolidFireRequestException as ex:
                ctx.log(ex.msg[1]['error']['message'])
                pass


@cli.command('purge', short_help='Purges the specified deleted volume(s).')
@click.argument('volumes',
                nargs=-1,
                required=True)
@pass_context
def purge(ctx, volumes):
    """Purge the specified deleted volumeID(s)."""
    for vid in volumes:
        try:
            ctx.sfapi.purge_deleted_volume(vid)
        except SolidFireRequestException as ex:
            ctx.log(ex.msg[1]['error']['message'])
            pass


@cli.command('show', short_help='Show detailed info for a single volume')
@click.argument('volume-id',
                required=True)
@pass_context
def show(ctx, volume_id):
    vol = _get_volume(ctx, volume_id)
    qos = vol['qos']
    # TODO(jdg): Add an option for curve, and figure
    # out a way to display it.  For now just remove it
    qos.pop('curve', None)
    cli_utils.print_dict(vol)


@cli.command('create', short_help='Creates a volume(s)')
@click.argument('size',
                required=True)
@click.option('--account-id',
              required=True,
              type=int,
              help='Account ID for the owner of this volume.')
@click.option('--name',
              required=True,
              help='Name of the new volume.')
@click.option('--enable512e/--no512e',
              default=True,
              help='Enable 512 byte emulation.')
@click.option('--attributes',
              default=None,
              help='Key Value pairs to set volume attributes '
                   '(--attributes attrName=val1,attrName2=val2...)')
@click.option('--qos',
              default=None,
              help='Key Value pairs to set QoS '
              '(--qos minIOPS=700,maxIOPS=900,burstIOPS=1000)')
@click.option('--count',
              default=1,
              help='Number of volumes to create.')
@pass_context
def create(ctx, size, account_id, name,
           enable512e=True, attributes=None,
           qos=None, count=1):
    """Creates <count> volumes of <size> on the SolidFire Cluster.

        Where size can be specified in bytes GibiBytes or GigaBytes
        (1073741824 | 1Gi | 1G).
    """
    vol_ids = []
    size = utils.string_to_bytes(size)
    if qos:
        qos = utils.kv_string_to_dict(qos)
        for k, v in qos.iteritems():
            qos[k] = int(v)
    if attributes:
        import pdb;pdb.set_trace()
        attributes = utils.kv_string_to_dict(attributes)

    vname = name
    for i in xrange(0, int(count)):
        if i > 0:
            vname = name + ('-%s' % i)
        vol_ids.append(ctx.sfapi.create_volume(vname, account_id,
                                               size, enable512e,
                                               qos, attributes))
    for vid in vol_ids:
        vol = _get_volume(ctx, vid)
        qos = vol['qos']
        qos.pop('curve', None)
        cli_utils.print_dict(vol)


@cli.command('clone', short_help='Clones a volume(s)')
@click.argument('volume-id',
                required=True)
@click.option('--from-snapshot',
              type=int,
              default=None,
              help='Use the specified Snapshot contents for Clone.')
@click.option('--name',
              required=True,
              help='Name of the new volume.')
@click.option('--new-account-id',
              required=False,
              type=int,
              help='Assign clone to different account ID than original.')
@click.option('--new-size',
              required=False,
              type=int,
              help='New size of the volume.')
@click.option('--attributes',
              default=None,
              help='Key Value pairs to set volume attributes '
                   '(--attributes attrName=val1,attrName2=val2...)')
@click.option('--access',
              default='readWrite',
              help='Access allowed for new cloned volume '
                   '(readOnly, readWrite, locked, replicationTarget)')
@click.option('--count',
              default=1,
              help='Number of clones to create.')
@pass_context
def clone(ctx, volume_id, name, from_snapshot,
          new_account_id=None, new_size=None,
          attributes=None, access='rw', count=1):
    """Creates <count> clones of volume specified by volume-id."""
    vol_ids = []
    if attributes:
        attributes = utils.kv_string_to_dict(attributes)
    clone_name = name
    for i in xrange(0, int(count)):
        if i > 0:
            clone_name = name + ('-%s' % i)
        vol_ids.append(ctx.sfapi.clone_volume(volume_id, clone_name,
                                              new_account_id=new_account_id,
                                              new_size=new_size,
                                              access=access,
                                              snapshot_id=from_snapshot,
                                              attributes=attributes))
    for vid in vol_ids:
        vol = _get_volume(ctx, vid)
        qos = vol['qos']
        qos.pop('curve', None)
        cli_utils.print_dict(vol)


@cli.command('stats', short_help='Show stats for the specified volume')
@click.argument('volume-id',
                required=True)
@pass_context
def stats(ctx, volume_id):
    stats_info = ctx.sfapi.get_volume_stats(volume_id)['volumeStats']
    cli_utils.print_dict(stats_info)


@cli.command('uuids', short_help='List mismatched UUIDs.')
@click.option('--accounts',
              default=None,
              help='List only for the specified list of account ID\'s.')
@pass_context
def uuids(ctx, accounts=None):
    """List Volumes."""
    volumes = _list_volumes(ctx, accounts, False)
    mismatched = []
    for v in volumes:
        if v['attributes']:
            meta_uuid = v['attributes'].get('uuid', {})
            if meta_uuid and meta_uuid not in v['name']:
                mismatched.append({'ID': v['volumeID'],
                                   'Name': v['name'],
                                   'Attributes-UUID': meta_uuid})

    key_list = ['ID', 'Name', 'Attributes-UUID']
    cli_utils.print_list(mismatched, key_list)
