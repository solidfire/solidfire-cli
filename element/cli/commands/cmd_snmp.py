#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright &copy; 2014-2016 NetApp, Inc. All Rights Reserved.
#
# DO NOT EDIT THIS CODE BY HAND! It has been generated with jsvcgen.
#

import click

from element.cli import utils as cli_utils
from element.cli import parser
from element.cli.cli import pass_context
from element import utils
import jsonpickle
import simplejson
from solidfire.models import *
from solidfire.custom.models import *
from uuid import UUID
from element import exceptions
from solidfire import common
from element.cli.cli import SolidFireOption, SolidFireCommand

@click.group()
@pass_context
def cli(ctx):
    """enable getacl getinfo gettrapinfo sendtesttraps getstate disable settrapinfo setinfo setacl """

@cli.command('enable', short_help="""EnableSnmp enables you to enable SNMP on cluster nodes. When you enable SNMP, the action applies to all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to EnableSnmp. """, cls=SolidFireCommand)
@click.option('--snmpv3enabled',
              type=bool,
              required=True,
              prompt=True,
              help="""If set to "true", then SNMP v3 is enabled on each node in the cluster. If set to "false", then SNMP v2 is enabled. """)
@pass_context
def enable(ctx,
           # Mandatory main parameter
           snmpv3enabled):
    """EnableSnmp enables you to enable SNMP on cluster nodes. When you enable SNMP, the action applies to all nodes in the cluster, and"""
    """the values that are passed replace, in whole, all values set in any previous call to EnableSnmp."""

    

    cli_utils.establish_connection(ctx)
    
    

    ctx.logger.info(""": """"""snmpv3enabled = """ + str(snmpv3enabled)+""";"""+"")
    try:
        _EnableSnmpResult = ctx.element.enable_snmp(snmp_v3_enabled=snmpv3enabled)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_EnableSnmpResult), indent=4))
        return
    else:
        cli_utils.print_result(_EnableSnmpResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getacl', short_help="""GetSnmpACL enables you to return the current SNMP access permissions on the cluster nodes. """, cls=SolidFireCommand)
@pass_context
def getacl(ctx):
    """GetSnmpACL enables you to return the current SNMP access permissions on the cluster nodes."""

    

    cli_utils.establish_connection(ctx)
    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetSnmpACLResult = ctx.element.get_snmp_acl()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetSnmpACLResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetSnmpACLResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getinfo', short_help="""GetSnmpInfo enables you to retrieve the current simple network management protocol (SNMP) configuration information. Note: GetSnmpInfo is available for Element OS 8 and prior releases. It is deprecated for versions later than Element OS 8. NetApp recommends that you migrate to the GetSnmpState and SetSnmpACL methods. See details in the Element API Reference Guide for their descriptions and usage. """, cls=SolidFireCommand)
@pass_context
def getinfo(ctx):
    """GetSnmpInfo enables you to retrieve the current simple network management protocol (SNMP) configuration information."""
    """Note: GetSnmpInfo is available for Element OS 8 and prior releases. It is deprecated for versions later than Element OS 8."""
    """NetApp recommends that you migrate to the GetSnmpState and SetSnmpACL methods. See details in the Element API Reference Guide"""
    """for their descriptions and usage."""

    

    cli_utils.establish_connection(ctx)
    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetSnmpInfoResult = ctx.element.get_snmp_info()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetSnmpInfoResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetSnmpInfoResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('gettrapinfo', short_help="""You can use GetSnmpTrapInfo to return current SNMP trap configuration information. """, cls=SolidFireCommand)
@pass_context
def gettrapinfo(ctx):
    """You can use GetSnmpTrapInfo to return current SNMP trap configuration information."""

    

    cli_utils.establish_connection(ctx)
    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetSnmpTrapInfoResult = ctx.element.get_snmp_trap_info()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetSnmpTrapInfoResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetSnmpTrapInfoResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('sendtesttraps', short_help="""SnmpSendTestTraps enables you to test SNMP functionality for a cluster. This method instructs the cluster to send test SNMP traps to the currently configured SNMP manager. """, cls=SolidFireCommand)
@pass_context
def sendtesttraps(ctx):
    """SnmpSendTestTraps enables you to test SNMP functionality for a cluster. This method instructs the cluster to send test SNMP traps to the currently configured SNMP manager."""

    

    cli_utils.establish_connection(ctx)
    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _SnmpSendTestTrapsResult = ctx.element.snmp_send_test_traps()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_SnmpSendTestTrapsResult), indent=4))
        return
    else:
        cli_utils.print_result(_SnmpSendTestTrapsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getstate', short_help="""You can use GetSnmpState to return the current state of the SNMP feature. """, cls=SolidFireCommand)
@pass_context
def getstate(ctx):
    """You can use GetSnmpState to return the current state of the SNMP feature."""

    

    cli_utils.establish_connection(ctx)
    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetSnmpStateResult = ctx.element.get_snmp_state()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetSnmpStateResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetSnmpStateResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('disable', short_help="""You can use DisableSnmp to disable SNMP on the cluster nodes. """, cls=SolidFireCommand)
@pass_context
def disable(ctx):
    """You can use DisableSnmp to disable SNMP on the cluster nodes."""

    

    cli_utils.establish_connection(ctx)
    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _DisableSnmpResult = ctx.element.disable_snmp()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_DisableSnmpResult), indent=4))
        return
    else:
        cli_utils.print_result(_DisableSnmpResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('settrapinfo', short_help="""You can use SetSnmpTrapInfo to enable and disable the generation of cluster SNMP notifications (traps) and to specify the set of network host computers that receive the notifications. The values you pass with each SetSnmpTrapInfo method call replace all values set in any previous call to SetSnmpTrapInfo. """, cls=SolidFireCommand)
@click.option('--traprecipients',
              cls=SolidFireOption,
              is_flag=True,
              multiple=True,
              subparameters=["host", "community", "port", ],
              required=True,
              help="""List of hosts that are to receive the traps generated by the Cluster Master. At least one object is required if any one of the trap types is enabled.  Has the following subparameters: --host --community --port """)
@click.option('--host',
              required=True,
              prompt=True,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] The IP address or host name of the target network management station. """,
              cls=SolidFireOption)
@click.option('--community',
              required=True,
              prompt=True,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] SNMP community string. """,
              cls=SolidFireOption)
@click.option('--port',
              required=True,
              prompt=True,
              multiple=True,
              type=int,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] The UDP port number on the host where the trap is to be sent. Valid range is 1 - 65535. 0 (zero) is not a valid port number. Default is 162. """,
              cls=SolidFireOption)
@click.option('--clusterfaulttrapsenabled',
              type=bool,
              required=True,
              prompt=True,
              help="""If the value is set to true, a corresponding solidFireClusterFaultNotification is sent to the configured list of trap recipients when a cluster fault is logged. The default value is false. """)
@click.option('--clusterfaultresolvedtrapsenabled',
              type=bool,
              required=True,
              prompt=True,
              help="""If the value is set to true, a corresponding solidFireClusterFaultResolvedNotification is sent to the configured list of trap recipients when a cluster fault is resolved. The default value is false. """)
@click.option('--clustereventtrapsenabled',
              type=bool,
              required=True,
              prompt=True,
              help="""If the value is set to true, a corresponding solidFireClusterEventNotification is sent to the configured list of trap recipients when a cluster event is logged. The default value is false. """)
@pass_context
def settrapinfo(ctx,
           # Mandatory main parameter
           traprecipients,
           # Mandatory main parameter
           clusterfaulttrapsenabled,
           # Mandatory main parameter
           clusterfaultresolvedtrapsenabled,
           # Mandatory main parameter
           clustereventtrapsenabled,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           host,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           community,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           port):
    """You can use SetSnmpTrapInfo to enable and disable the generation of cluster SNMP notifications (traps) and to specify the set of network host computers that receive the notifications. The values you pass with each SetSnmpTrapInfo method call replace all values set in any previous call to SetSnmpTrapInfo."""

    

    cli_utils.establish_connection(ctx)
    

    traprecipientsArray = None
    if len(traprecipients) == 1 and host[0] is None and community[0] is None and port[0] is None:
        traprecipientsArray = []
    elif(traprecipients is not None and traprecipients != ()):
        traprecipientsArray = []
        try:
            for i, _traprecipients in enumerate(traprecipients):
                traprecipientsArray.append(SnmpTrapRecipient(host=host[i], community=community[i], port=port[i], ))
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    
    
    
    

    ctx.logger.info(""": """"""traprecipients = """ + str(traprecipientsArray)+";"+"""clusterfaulttrapsenabled = """ + str(clusterfaulttrapsenabled)+";"+"""clusterfaultresolvedtrapsenabled = """ + str(clusterfaultresolvedtrapsenabled)+";"+"""clustereventtrapsenabled = """ + str(clustereventtrapsenabled)+""";"""+"")
    try:
        _SetSnmpTrapInfoResult = ctx.element.set_snmp_trap_info(trap_recipients=traprecipientsArray, cluster_fault_traps_enabled=clusterfaulttrapsenabled, cluster_fault_resolved_traps_enabled=clusterfaultresolvedtrapsenabled, cluster_event_traps_enabled=clustereventtrapsenabled)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_SetSnmpTrapInfoResult), indent=4))
        return
    else:
        cli_utils.print_result(_SetSnmpTrapInfoResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('setinfo', short_help="""SetSnmpInfo enables you to configure SNMP version 2 and version 3 on cluster nodes. The values you set with this interface apply to all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to SetSnmpInfo. Note: SetSnmpInfo is deprecated. Use the EnableSnmp and SetSnmpACL methods instead. """, cls=SolidFireCommand)
@click.option('--networks',
              cls=SolidFireOption,
              is_flag=True,
              multiple=True,
              subparameters=["accessnetworks", "cidr", "community", "network", ],
              required=False,
              help="""List of networks and what type of access they have to the SNMP servers running on the cluster nodes. See the SNMP Network Object for possible "networks" values. This parameter is required only for SNMP v2.  Has the following subparameters: --accessnetworks --cidr --community --network """)
@click.option('--accessnetworks',
              required=False,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] ro: read-only access.* rw: for read-write access. rosys: for read-only access to a restricted set of system information *SolidFire recommends that all networks other than the default "localhost" be set to "ro" access, because all SolidFire MIB objects are read-only. """,
              cls=SolidFireOption)
@click.option('--cidr',
              required=False,
              multiple=True,
              type=int,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] A CIDR network mask. This network mask must be an integer greater than or equal to 0, and less than or equal to 32. It must also not be equal to 31. """,
              cls=SolidFireOption)
@click.option('--community',
              required=False,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] SNMP community string. """,
              cls=SolidFireOption)
@click.option('--network',
              required=False,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] This parameter ainteger with the cidr variable is used to control which network the access and community string apply to. The special value of "default" is used to specify an entry that applies to all networks. The cidr mask is ignored when network value is either a host name or default. """,
              cls=SolidFireOption)
@click.option('--enabled',
              type=bool,
              required=False,
              help="""If set to true, SNMP is enabled on each node in the cluster. """)
@click.option('--snmpv3enabled',
              type=bool,
              required=False,
              help="""If set to true, SNMP v3 is enabled on each node in the cluster. """)
@click.option('--usmusers',
              cls=SolidFireOption,
              is_flag=True,
              multiple=True,
              subparameters=["accessusmusers", "name", "password", "passphrase", "seclevel", ],
              required=False,
              help="""If SNMP v3 is enabled, this value must be passed in place of the networks parameter. This parameter is required only for SNMP v3.  Has the following subparameters: --accessusmusers --name --password --passphrase --seclevel """)
@click.option('--accessusmusers',
              required=False,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] rouser: read-only access.* rwuser: for read-write access. rosys: for read-only access to a restricted set of system information *SolidFire recommends that all USM users be set to "rouser" access, because all SolidFire MIB objects are read-only. """,
              cls=SolidFireOption)
@click.option('--name',
              required=False,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] The name of the user. Must contain at least one character, but no more than 32 characters. Blank spaces are not allowed. """,
              cls=SolidFireOption)
@click.option('--password',
              required=False,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] The password of the user. Must be between 8 and 255 characters integer (inclusive). Blank spaces are not allowed. Required if "secLevel" is "auth" or "priv." """,
              cls=SolidFireOption)
@click.option('--passphrase',
              required=False,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] The passphrase of the user. Must be between 8 and 255 characters integer (inclusive). Blank spaces are not allowed. Required if "secLevel" is "priv." """,
              cls=SolidFireOption)
@click.option('--seclevel',
              required=False,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] noauth: No password or passphrase is required. auth: A password is required for user access. priv: A password and passphrase is required for user access. """,
              cls=SolidFireOption)
@pass_context
def setinfo(ctx,
           # Optional main parameter
           networks = None,
           # Optional subparameter of optional main parameter.
           accessnetworks = None,
           # Optional subparameter of optional main parameter.
           cidr = None,
           # Optional subparameter of optional main parameter.
           community = None,
           # Optional subparameter of optional main parameter.
           network = None,
           # Optional main parameter
           enabled = None,
           # Optional main parameter
           snmpv3enabled = None,
           # Optional main parameter
           usmusers = None,
           # Optional subparameter of optional main parameter.
           accessusmusers = None,
           # Optional subparameter of optional main parameter.
           name = None,
           # Optional subparameter of optional main parameter.
           password = None,
           # Optional subparameter of optional main parameter.
           passphrase = None,
           # Optional subparameter of optional main parameter.
           seclevel = None):
    """SetSnmpInfo enables you to configure SNMP version 2 and version 3 on cluster nodes. The values you set with this interface apply to"""
    """all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to SetSnmpInfo."""
    """Note: SetSnmpInfo is deprecated. Use the EnableSnmp and SetSnmpACL methods instead."""

    

    cli_utils.establish_connection(ctx)
    

    networksArray = None
    if len(networks) == 1 and accessnetworks[0] is None and cidr[0] is None and community[0] is None and network[0] is None:
        networksArray = []
    elif(networks is not None and networks != ()):
        networksArray = []
        try:
            for i, _networks in enumerate(networks):
                networksArray.append(SnmpNetwork(access=accessnetworks[i], cidr=cidr[i], community=community[i], network=network[i], ))
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    
    
    

    usmusersArray = None
    if len(usmusers) == 1 and accessusmusers[0] is None and name[0] is None and password[0] is None and passphrase[0] is None and seclevel[0] is None:
        usmusersArray = []
    elif(usmusers is not None and usmusers != ()):
        usmusersArray = []
        try:
            for i, _usmusers in enumerate(usmusers):
                usmusersArray.append(SnmpV3UsmUser(access=accessusmusers[i], name=name[i], password=password[i], passphrase=passphrase[i], sec_level=seclevel[i], ))
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    

    ctx.logger.info(""": """"""networks = """+str(networksArray)+";" + """enabled = """+str(enabled)+";" + """snmpv3enabled = """+str(snmpv3enabled)+";" + """usmusers = """+str(usmusersArray)+""";"""+"")
    try:
        _SetSnmpInfoResult = ctx.element.set_snmp_info(networks=networksArray, enabled=enabled, snmp_v3_enabled=snmpv3enabled, usm_users=usmusersArray)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_SetSnmpInfoResult), indent=4))
        return
    else:
        cli_utils.print_result(_SetSnmpInfoResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('setacl', short_help="""SetSnmpACL enables you to configure SNMP access permissions on the cluster nodes. The values you set with this interface apply to all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to SetSnmpACL. Also note that the values set with this interface replace all network or usmUsers values set with the older SetSnmpInfo. """, cls=SolidFireCommand)
@click.option('--networks',
              cls=SolidFireOption,
              is_flag=True,
              multiple=True,
              subparameters=["accessnetworks", "cidr", "community", "network", ],
              required=True,
              help="""List of networks and what type of access they have to the SNMP servers running on the cluster nodes. See SNMP Network Object for possible "networks" values. This parameter is required if SNMP v3 is disabled.  Has the following subparameters: --accessnetworks --cidr --community --network """)
@click.option('--accessnetworks',
              required=True,
              prompt=True,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] ro: read-only access.* rw: for read-write access. rosys: for read-only access to a restricted set of system information *SolidFire recommends that all networks other than the default "localhost" be set to "ro" access, because all SolidFire MIB objects are read-only. """,
              cls=SolidFireOption)
@click.option('--cidr',
              required=True,
              prompt=True,
              multiple=True,
              type=int,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] A CIDR network mask. This network mask must be an integer greater than or equal to 0, and less than or equal to 32. It must also not be equal to 31. """,
              cls=SolidFireOption)
@click.option('--community',
              required=True,
              prompt=True,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] SNMP community string. """,
              cls=SolidFireOption)
@click.option('--network',
              required=True,
              prompt=True,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] This parameter ainteger with the cidr variable is used to control which network the access and community string apply to. The special value of "default" is used to specify an entry that applies to all networks. The cidr mask is ignored when network value is either a host name or default. """,
              cls=SolidFireOption)
@click.option('--usmusers',
              cls=SolidFireOption,
              is_flag=True,
              multiple=True,
              subparameters=["accessusmusers", "name", "password", "passphrase", "seclevel", ],
              required=True,
              help="""List of users and the type of access they have to the SNMP servers running on the cluster nodes.  Has the following subparameters: --accessusmusers --name --password --passphrase --seclevel """)
@click.option('--accessusmusers',
              required=True,
              prompt=True,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] rouser: read-only access.* rwuser: for read-write access. rosys: for read-only access to a restricted set of system information *SolidFire recommends that all USM users be set to "rouser" access, because all SolidFire MIB objects are read-only. """,
              cls=SolidFireOption)
@click.option('--name',
              required=True,
              prompt=True,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] The name of the user. Must contain at least one character, but no more than 32 characters. Blank spaces are not allowed. """,
              cls=SolidFireOption)
@click.option('--password',
              required=True,
              prompt=True,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] The password of the user. Must be between 8 and 255 characters integer (inclusive). Blank spaces are not allowed. Required if "secLevel" is "auth" or "priv." """,
              cls=SolidFireOption)
@click.option('--passphrase',
              required=True,
              prompt=True,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] The passphrase of the user. Must be between 8 and 255 characters integer (inclusive). Blank spaces are not allowed. Required if "secLevel" is "priv." """,
              cls=SolidFireOption)
@click.option('--seclevel',
              required=True,
              prompt=True,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] noauth: No password or passphrase is required. auth: A password is required for user access. priv: A password and passphrase is required for user access. """,
              cls=SolidFireOption)
@pass_context
def setacl(ctx,
           # Mandatory main parameter
           networks,
           # Mandatory main parameter
           usmusers,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           accessnetworks,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           cidr,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           community,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           network,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           accessusmusers,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           name,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           password,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           passphrase,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           seclevel):
    """SetSnmpACL enables you to configure SNMP access permissions on the cluster nodes. The values you set with this interface apply to all"""
    """nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to SetSnmpACL. Also note"""
    """that the values set with this interface replace all network or usmUsers values set with the older SetSnmpInfo."""

    

    cli_utils.establish_connection(ctx)
    

    networksArray = None
    if len(networks) == 1 and accessnetworks[0] is None and cidr[0] is None and community[0] is None and network[0] is None:
        networksArray = []
    elif(networks is not None and networks != ()):
        networksArray = []
        try:
            for i, _networks in enumerate(networks):
                networksArray.append(SnmpNetwork(access=accessnetworks[i], cidr=cidr[i], community=community[i], network=network[i], ))
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    

    usmusersArray = None
    if len(usmusers) == 1 and accessusmusers[0] is None and name[0] is None and password[0] is None and passphrase[0] is None and seclevel[0] is None:
        usmusersArray = []
    elif(usmusers is not None and usmusers != ()):
        usmusersArray = []
        try:
            for i, _usmusers in enumerate(usmusers):
                usmusersArray.append(SnmpV3UsmUser(access=accessusmusers[i], name=name[i], password=password[i], passphrase=passphrase[i], sec_level=seclevel[i], ))
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    

    ctx.logger.info(""": """"""networks = """ + str(networksArray)+";"+"""usmusers = """ + str(usmusersArray)+""";"""+"")
    try:
        _SetSnmpACLResult = ctx.element.set_snmp_acl(networks=networksArray, usm_users=usmusersArray)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_SetSnmpACLResult), indent=4))
        return
    else:
        cli_utils.print_result(_SetSnmpACLResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

