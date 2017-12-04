SolidFire CLI Tools for Storage Clusters
=================================================
This tool is intended to be an easy-to-use command-line interface that enables you to do the following:

1. Quickly install a fully functional interface to the JSON-RPC using pip.
2. Get help on how to use the commands by accessing the inline help.
3. Execute any command supported by NetApp SolidFire Element OS.
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

Note: If you are on a Linux OS, you will have to set up a virtual environment first because the native linux python does not support setuptools. To create a virtual environment, run:

    pip install virtualenv
    virtualenv pythoncli
    source pythoncli/bin/activate # This activates the virtual environment. 

**Installation Steps**

To install from pypi using pip, execute the following command:

    pip install solidfire-cli

-- or --

To install from source using easy_install, navigate to solidfirecli*.tar.gz file (where the * stands for the version), and run

	easy_install solidfirecli*.tar.gz

___

**SolidFire CLI Tools as Docker Container**

To **start** a new container from our published image, use the following:

    >: docker run -it netapp/solidfire-cli bin/bash

You can **run** commands in the newly started container using standard sfcli commands from within it with the `bash-4.3#` prompt.

-- or --

To **run** sfcli commands from the host on a running container, use the following: 

    >: docker exec [container_name] [sfcli command] 

Replace `[sfcli command]` with whichever cli command you are wanting to run. 

Supported Operating Systems
-----------------------------------
* Windows 7, 8, and 10
* Linux
* MacOS

## Documentation

[User Guide](https://solidfire.github.io/solidfire-cli/NetApp_SolidFire_CLI_User_Guide.pdf) This readme in .pdf form.

[Release Notes](https://solidfire.github.io/solidfire-cli/NetApp_SolidFire_CLI_Release_Notes.pdf) v1.5

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
In the following example, the --volumes parameter has subparameters, such as volumeid, accessvolumes, name, newaccountid, newsize, and attributes:

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

Known Issues
---------------
Here are the known issues. This list will be added to while they are open. Known issues will be removed from here if/when are fixed.

- Cannot pass blank strings for **schedule** command parameters (or any other commands, actually). 
  - If you need to blank out a value, it is currently impossible to pass blank strings via sfcli. Instead, you will need to either a) use a character that represents a blank (eg. _ or *) or b) use one of the other Host Integraion or User Interface tools.
- NEVER use `sudo` to `pip install solidfire-cli`! [Here](https://stackoverflow.com/questions/33004708/osx-el-capitan-sudo-pip-install-oserror-errno-1-operation-not-permitted/33004920#33004920) is a good explanation of why that is a bad idea. 
  - Anyone on Linux should expect to use a virtual env.
  - Windows and Mac users can get away without virtual envs.
