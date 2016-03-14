Python Lib and CLI for SolidFire Storage Clusters
=================================================

This is a Command-Line Client and Python Library for the SolidFire API.
The Client Utility is intended to provide a quick and easy Command Line
interface to interact with the SolidFire API and is made of up
wrapper/helper methods to enable a user to do a number of things more
easily with their Cluster.

The Python Libraries implement the same methods that are used by the
Client, however in addition they also provide the ability to simply call
the SolidFire API method directly. In most cases each will simply take a
dictionary which is the API parameters. This should follow the Element
API Reference Guide, and simply provide some wrappers around the calls
to make automation easier.

Check out the specific sections and examples below.

NOTE: This is very much a work in progress, the idea started over a year
ago and just finally decided to try it out on a VERY cold and snowy day
after Christmas.

Installation
------------

These modules are still in early development and while available in
private git repo, they are not currently being published to PyPI
(hopefully they will be).

Best way to install is from source and using venv:

1. `git clone https://github.com/j-griffith/python-solidfireclient`
2. `cd python-solidfireclient`
3. `virtualenv venv`
4. `source venv/bin/activate`
5. `pip install -e .`
6.  Modify `sfvars.env` appropriately
7. `source sfvars.env`
8. `sfcli

Command-Line Usage
------------------

To use the Command-Line you will need to source an rc file for
your cluster endpont info and credentials.

    export mvip=172.16.140.21
    export login=admin
    export password=admin
    export port=443
    export url=https://100.16.146.20:443

Help/Documentation for using the shell is also available by running

`sfcli --help`:
    Usage: sfcli [OPTIONS] COMMAND [ARGS]...

      SolidFire command line interface.

    Options:
      -m, --mvip TEXT            SolidFire MVIP
      -l, --login TEXT           SolidFire Cluster login
      -p, --password TEXT        SolidFire cluster password
      --format [table|raw|json]  Output format
      -c, --conf PATH            Config file location
      --debug [0|1|2|3]          Set the debug level
      -v, --verbose              Provide extra output info
      --timings                  Time each API call and display after results
      --help                     Show this message and exit.

    Commands:
      accounts  Account methods.
      volumes   Volume methods.

Example command to show details on a specified volume:

    solidfire volume-show 30943
    +--------------------+--------------------------------------------------------------------------------+
    |      Property      |                                     Value                                      |
    +--------------------+--------------------------------------------------------------------------------+
    |       access       |                                   readWrite                                    |
    |     accountID      |                                     12661                                      |
    |     attributes     |                                       {}                                       |
    |     createTime     |                              2014-12-31T02:44:52Z                              |
    |     deleteTime     |                                                                                |
    |     enable512e     |                                      True                                      |
    |        iqn         | iqn.2010-01.com.solidfire:9kdb.uuid-56a2bab0-5223-4fc5-ba4d-0595820ec453.30943 |
    |        name        |                   UUID-56a2bab0-5223-4fc5-ba4d-0595820ec453                    |
    |     purgeTime      |                                                                                |
    |  scsiEUIDeviceID   |                        396b6462000078dff47acc0100000000                        |
    |  scsiNAADeviceID   |                        6f47acc100000000396b6462000078df                        |
    |     sliceCount     |                                       1                                        |
    |       status       |                                     active                                     |
    |     totalSize      |                                   1073741824                                   |
    | volumeAccessGroups |                                       []                                       |
    |      volumeID      |                                     30943                                      |
    |    volumePairs     |                                       []                                       |
    +--------------------+--------------------------------------------------------------------------------+

Python API-Lib
--------------

Currently the only useful component in terms of Python libs is the
solidfire_element_api module.  In the future more modules will be
added to solidire/managers directory.

Example using the Python libs:

    >>> from solidfire import solidfire_element_api as api
    >>> endpoint_info = {'mvip': 192.168.140.5, 'login': 'admin',
                         'password': 'SuperDooperPassword!', 'port': 443,
                         'url': 'https://192.168.140.5:443'}
    >>> sf_client = api.SolidFireAPI(endpoint_info)
    >>> sf_client.volumes.show(23596)
    {u'status': u'active', u'enable512e': True, u'qos': {u'burstIOPS': 15000, u'curve': {u'8192': 160, u'32768': 500, u'4096': 100, u'1048576': 15000, u'131072': 1950, u'262144': 3900, u'16384': 270, u'65536': 1000, u'524288': 7600}, u'minIOPS': 100, u'burstTime': 60, u'maxIOPS': 15000}, u'name': u'UUID-a8a501cb-dd29-46d5-8506-56b652de6055', u'volumeAccessGroups': [], u'totalSize': 1073741824, u'scsiNAADeviceID': u'6f47acc100000000396b646200005c2c', u'purgeTime': u'', u'scsiEUIDeviceID': u'396b646200005c2cf47acc0100000000', u'volumeID': 23596, u'access': u'readWrite', u'iqn': u'iqn.2010-01.com.solidfire:9kdb.uuid-a8a501cb-dd29-46d5-8506-56b652de6055.23596', u'sliceCount': 1, u'attributes': {u'created_at': u'2014-12-23T07:15:19.000000', u'attached_to': None, u'is_clone': u'False', u'attach_time': None, u'uuid': u'a8a501cb-dd29-46d5-8506-56b652de6055'}, u'volumePairs': [], u'deleteTime': u'', u'createTime': u'2014-12-23T07:15:20Z', u'accountID': 9573}
    >>>
