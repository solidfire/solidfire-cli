Python Lib and CLI for SolidFire Storage Clusters
=================================================
The purpose of this tool is not as a hard core programming language, but rather as a quick and dirty command line interface. This feature gives the user the ability to

1. Quickly install a fully functional interface to the JSON-RPC using pip
2. Learn how to use the commands by via inline help
3. Execute any command supported by Fluorine
4. Utilize autofill on MacOS and Linux distributions to make constructing commands easier
5. Get the responses in 3 different output formats: Tree format, Json format, and Pickle format
6. Execute any non-public command by using "sfcli sfapi invoke" with the necessary method name and parameters.
7. Achieve the same functionality as the SDKs without ever opening an editor.
8. Establish and store connection information locally

Intended Audience
-----------------
The SolidFire CLI is intended for users who for one reason or another, cannot or will
not use PowerShell. It integrates as you would expect with bash. The main advantages
of using this framework are (firstly) that the objects are returned as strings which
allows for expeditious grepping and (secondly) that it is very easy to install and get
set up.

To Install
----------
pip install solidfire-cli

Operating Systems and Distributions
-----------------------------------
Windows 7, 8, 10, Linux, Mac

Accessing Inline Help
---------------------
To see top level help, run:

    sfcli --help

To see second level help, run:

    sfcli account --help

To see commands specific help, run:

    sfcli account getbyid --help

Enabling Autocomplete
---------------------
Copy and paste the following into your .bashrc file or run it whenever you want autocomplete enabled:

    eval "$(_SFCLI_COMPLETE=source sfcli)"

Connection Management
---------------------
To run a command on a given connection without storing it away, use the mvip, login, and password options.

    sfcli --mvip 10.117.60.15 --login admin --password admin Account List

To store a given connection, use the Connection Push and supply the name option.

    sfcli --mvip 10.117.60.15 --login admin --password admin --name "Example" Connection Push

To use a connection you've stored, use -n or --name or -c or -connectionIndex or leave it to default to connection 0

    sfcli -n Example Account List # by name
    sfcli -c 0 Account List # by index
    sfcli Account List # use connection 0

To remove a given connection, use the Connection Remove command.

    sfcli Connection Remove -n Example
    sfcli Connection Remove -i -1 # Removes the newly pushed connection.
    sfcli Connection Remove -i 0 # Removes the oldest pushed connection.
    sfcli Connection Remove -i 1 # Removes the second oldest connection.

To list the stored connections, use the Connection List command.

	sfcli Connection List

To prune broken connections from the connection.csv file, use the Connection Prune command.

	sfcli Connection Prune

Executing Commands
------------------
Executing a command with standard parameters:

    sfcli -c 0 Account GetByID --account_id 94

Executing Commands with Grouped Parameters
------------------------------------------
Occasionally, the docs will refer to something called a subparameter. A subparameter
is used to specify an attribute of a super parameter. For instance,

    sfcli volume clonemultiple --help

    Usage: sfcli volume clonemultiple [OPTIONS]

      CloneMultipleVolumes is used to create a clone of a group of specified
      volumes. A consistent set of characteristics can be assigned to a group of
      multiple volume when they are cloned together.

    Options:
      --volumes                      Array of Unique ID for each volume to include
                                     in the clone with optional parameters. If
                                     optional parameters are not specified, the
                                     values will be inherited from the source
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
      --attributes TEXT              [subparameter] List of Name/Value pairs in
                                     JSON object format.
      --access TEXT                  New default access method for the new volumes
                                     if not overridden by information passed in
                                     the volumes array. readOnly: Only read
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

If I want to clone multipe volumes in the same group, I can run it as follows:

    sfcli volume clonemultiple --volumes --volumeid 1 --accessvolumes readWrite --volumes --volumeid 1

This will clone the volumes and apply the readWrite access to volume 1 and use the default for volume 2.

Executing Commands with Non-Standard Parameters
------------------------------------------------
Occasionally, the user will need to pass in an arbitrary dictionary of keys and values. In that case,
the user will need to provide a json string directly to the command line.

In the example below, if you want to bypass the logic and send somethign directly to the api, you can
do so by using SFApi Invoke.

#### SFApi Invoke ####

    $account = sfcli -c 0 SFApi Invoke --method GetAccountByID --parameters '{\"accountID\":94}'

Output Formats
--------------
#### Tree Format (Default) ####
The tree format was constructed specifically to make it easier for users to grep the output and get
a result without extra formatting. It uses whitespace to distinguish between different objects. To
view this format, one need only run a command without the -j or -k flags.

Example:

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
            username:   ARIEL

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

#### Json Format ####
The json format is constructed to look like the output of the api. This can be useful if you are going
to store the data away for later use with postman or if you want to import it via any json libraries.
To get this output, add the flag, -j after "sfcli" in your command.

Example:

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
                "username": "ARIEL",
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
The pickle format is the same as the json format except with an extra field in every object.
This field names the object type. This is useful if you want to store the data away and use
it with a python sdk later. If you unpickle the string using the python sdk, you will get
a full object model instead of a nested dictionary. To use this, add the flag -k to your
command after "sfcli".

Example:

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
                "username": "ARIEL",
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


Command Details
---------------
Usage: sfcli [OPTIONS] COMMAND [ARGS]...

  SolidFire command line interface.

Options:

    -m, --mvip TEXT
        SolidFire MVIP
    -l, --login TEXT
        SolidFire Cluster login
    -p, --password TEXT
        SolidFire cluster password
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