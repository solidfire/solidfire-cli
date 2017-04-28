from element.exceptions import *
import jsonpickle
import json as serializer
from pkg_resources import Requirement, resource_filename
import os
import csv
from Crypto.Cipher import ARC4
import base64
import base64
import socket
import getpass
from solidfire.factory import ElementFactory
from solidfire import Element

def kv_string_to_dict(kv_string):
    new_dict = {}
    items = kv_string.split(',')
    for item in items:
        kvs = item.split('=')
        new_dict[kvs[0]] = kvs[1]

def print_result(objs, log, as_json=False, as_pickle=False, depth=None, filter_tree=None):
    # There are 3 acceptable parameter sets to provide:
    # 1. json=True, depth=None, filter_tree=None
    # 2. json=False, depth=#, filter_tree=None
    # 3. json=False, depth=#, filter_tree=acceptable string

    # Error case
    if as_json and (depth is not None or filter_tree is not None):
        log.error("If you choose to print it as json, do not provide a depth or filter. Those are for printing it as a tree.")
        exit()

    # If json is true, we print it as json and return:
    if as_json == True or as_pickle == True:
        print_result_as_json(objs, as_pickle)
        return

    # If we have a filter, apply it.
    if filter_tree is not None:
        try:
            objs_to_print = filter_objects_from_simple_keypaths(objs, filter_tree.split(','))
        except Exception as e:
            log.error(e.args[0])
            exit(1)
    else:
        objs_to_print = objs

    # Set up a default depth
    if depth is None:
        depth = 3

    # Next, print the tree to the appropriate depth
    print_result_as_tree(objs_to_print, depth)

def print_result_as_json(objs, pickle=False):
    #print(jsonpickle.encode(objs))
    nestedDict = serializer.loads(jsonpickle.encode(objs))
    filteredDict = type(nestedDict)()
    if(pickle==False):
        remove_pickling(nestedDict, filteredDict)
    else:
        filteredDict = nestedDict
    print(serializer.dumps(filteredDict,indent=4))

def remove_pickling(nestedDict, filteredDict):
    if type(nestedDict) is dict:
        #foreach key, if list, recurse, if dict, recurse, if string recurse unless py/obj is key.
        for key in nestedDict:
            if key == "py/object":
                continue
            else:
                filteredDict[key] = type(nestedDict[key])()
                filteredDict[key] = remove_pickling(nestedDict[key], filteredDict[key])
        return filteredDict
    if type(nestedDict) is list:
        # foreach item
        for i in range(len(nestedDict)):
            filteredDict.append(type(nestedDict[i])())
            filteredDict[i] = remove_pickling(nestedDict[i], filteredDict[i])
        return filteredDict
    return nestedDict

def get_result_as_tree(objs, depth=1, currentDepth=0, lastKey = ""):
    stringToReturn = ""
    if(currentDepth > depth):
        return "<to see more details, increase depth>\n"
    if(type(objs) is str or type(objs) is bool or type(objs) is int or type(objs) is type(u'') or objs is None):
        return str(objs) + "\n"
    if(type(objs) is list):
        stringToReturn += "\n"
        for i in range(len(objs)):
            obj = objs[i]
            stringToReturn += currentDepth*"    "+get_result_as_tree(obj, depth, currentDepth+1, lastKey)
        return stringToReturn
    if(type(objs) is dict):
        stringToReturn += "\n"
        for key in objs:
            stringToReturn += currentDepth*"    "+key+":   "+get_result_as_tree(objs[key], depth, currentDepth+1, key)
        return stringToReturn
    if(objs is None):
        return stringToReturn
    mydict = objs.__dict__
    stringToReturn += "\n"
    for key in mydict:
        stringToReturn += currentDepth*"    "
        stringToReturn += key+":   "+get_result_as_tree(mydict[key], depth, currentDepth+1, key)
    return stringToReturn

def filter_objects_from_simple_keypaths(objs, simpleKeyPaths):
    # First, we assemble the key paths.
    # They start out like this:
    # [accouts.username, accounts.initiator_secret.secret, accounts.status]
    # and become like this:
    # {"accounts":{"username":True, "initiator_secret":{"secret":True}, "status":True}
    keyPaths = dict()
    for simpleKeyPath in simpleKeyPaths:
        currentLevel = keyPaths
        keyPathArray = simpleKeyPath.split('.')
        for i in range(len(keyPathArray)):
            if(i<(len(keyPathArray) - 1)):
                if currentLevel.get(keyPathArray[i]) is None:
                    currentLevel[keyPathArray[i]] = dict()
            else:
                currentLevel[keyPathArray[i]] = True
            currentLevel = currentLevel[keyPathArray[i]]

    # Then we pass it in to filter objects.
    return filter_objects(objs, keyPaths)


# Keypaths is arranged as follows:
# it is a nested dict with the order of the keys.
def filter_objects(objs, keyPaths):
    # Otherwise, we keep recursing deeper.
    # Because there are deeper keys, we know that we can go deeper.
    # This means we are dealing with either an array or a dict.
    # If keyPaths looks like this:
    # {"username": True, "volumes": {"Id": True}}
    # The keys in this sequence will be username and volumes.
    # When we recurse into volumes, the keys will be Id.
    finalFilteredObjects = dict()
    if keyPaths == True and type(objs) is not list:
        return objs

    # If we've found a list, we recurse deeper to pull out the objs.
    # We do not advance our keyPath recursion because this is just a list.
    if type(objs) is list:
        # If we have a list of objects, we will need to assemble and return a list of stuff.
        filteredObjsDict = [None]*len(objs)
        for i in range(len(objs)):
            # Each element could be a string, dict, or list.
            filteredObjsDict[i] = filter_objects(objs[i], keyPaths)
        return filteredObjsDict

    dictionaryOfInterest = None
    if type(objs) is dict:
        dictionaryOfInterest = objs
    else:
        dictionaryOfInterest = objs.__dict__
    for key in keyPaths:
        # If we've found a dict, we recurse deeper to pull out the objs.
        # Because this is a dict, we must advance our keyPaths recursion.
        # Consider the following example:
        if key not in dictionaryOfInterest:
            raise ValueError("'"+key+"' is not a valid key for this level. Valid keys are: "+','.join(dictionaryOfInterest.keys()))
        print(dictionaryOfInterest[key])
        finalFilteredObjects[key] = filter_objects(dictionaryOfInterest[key], keyPaths[key])
    return finalFilteredObjects

def print_result_as_table(objs, keyPaths):
    filteredDictionary = filter_objects(objs, keyPaths)

def print_result_as_tree(objs, depth=1):
    print(get_result_as_tree(objs, depth))

def establish_connection(ctx):
    # Verify that the mvip does not contain the port number:
    if ctx.mvip and ":" in ctx.mvip:
        ctx.logger.error('Please provide the port using the port parameter.')
        exit(1)

    cfg = None
    # Arguments take precedence regardless of env settings
    if ctx.mvip:
        if ctx.username is None:
            ctx.username = getpass.getpass("Username:")
        if ctx.password is None:
            ctx.password = getpass.getpass("Password:")
        cfg = {'mvip': ctx.mvip,
               'username': ctx.username,
               'password': ctx.password,
               'port': ctx.port,
               'url': 'https://%s:%s' % (ctx.mvip, ctx.port),
               'version': ctx.version,
               'verifyssl': ctx.verifyssl}
        print(cfg)
        try:
            ctx.element = ElementFactory.create(cfg["mvip"],cfg["username"],cfg["password"],port=cfg["port"],version=cfg["version"],verify_ssl=cfg["verifyssl"])
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)

    # If someone accidentally passed in an argument, but didn't specify everything, throw an error.
    elif ctx.username or ctx.password:
        ctx.logger.error("In order to manually connect, please provide an mvip, a username, AND a password")

    # If someone asked for a given connection or we need to default to using the connection at index 0 if it exists:
    else:
        connections = get_connections()
        if(ctx.connectionindex is not None):
            if ctx.connectionindex > len(connections)-1 or ctx.connectionindex < (-len(connections)):
                ctx.logger.error("Please provide an index between "+str(-len(connections))+" and "+str(len(connections)-1))
                exit(1)
            cfg = connections[ctx.connectionindex]
        elif(ctx.name is not None):
            filteredCfg = [connection for connection in connections if connection["name"] == ctx.name]
            if(len(filteredCfg) > 1):
                ctx.logger.error("Your connections.csv file has become corrupted. There are two connections of the same name.")
                exit()
            if(len(filteredCfg) < 1):
                ctx.logger.error("Could not find a connection named "+ctx.name)
                exit()
            cfg = filteredCfg[0]
        else:
            if len(connections) > 0:
                cfg = connections[-1]

        # If we managed to find the connection we were looking for, we must try to establish the connection.
        if cfg is not None:
            # Finally, we need to establish our connection via elementfactory:
            try:
                if int(cfg["port"]) != 443:
                    address = cfg["mvip"] + ":" + cfg["port"]
                else:
                    address = cfg["mvip"]+ ":" + cfg["port"]
                ctx.element = Element(address, decrypt(cfg["username"]), decrypt(cfg["password"]), cfg["version"], verify_ssl=cfg["verifyssl"])
            except Exception as e:
                ctx.logger.error(e.__str__())
                ctx.logger.error("The connection is corrupt. Run 'sfcli connection prune' to try and remove all broken connections or use 'sfcli connection remove -n name'")
                ctx.logger.error(cfg)

    # If we want the json output directly from the source, we'll have to override the send request method in the sdk:
    if ctx.json and ctx.element:
        def new_send_request(*args, **kwargs):
            return ctx.element.__class__.__bases__[0].send_request(ctx.element, return_response_raw=True, *args, **kwargs)
        ctx.element.send_request = new_send_request

    # The only time it is none is when we're asking for help or we're trying to store a connection.
    # If that's not what we're doing, we catch it later.
    if cfg is not None:
        cfg["port"] = int(cfg["port"])
        ctx.cfg = cfg

    if ctx.element is None:
        ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
        exit()

def get_connections():
    connectionsCsvLocation = resource_filename(Requirement.parse("solidfire-cli"), "connections.csv")
    if os.path.exists(connectionsCsvLocation):
        with open(connectionsCsvLocation, 'r') as connectionFile:
            connections = list(csv.DictReader(connectionFile, delimiter=','))
    else:
        connections = []
    return connections

def write_connections(connections):
    connectionsCsvLocation = resource_filename(Requirement.parse("solidfire-cli"), "connections.csv")
    with open(connectionsCsvLocation, 'w') as f:
        w = csv.DictWriter(f, ["name","mvip","port","username","password","version","url","verifyssl"], lineterminator='\n')
        w.writeheader()
        for connection in connections:
            if connection is not None:
                w.writerow(connection)

# Split up something like this:
# name:value,name:value,name:value;name:value,name:value,name:value
# into something like this:
# [{name:value, name:value, name:value}, {name:value, name:value, name:value}]
def loads(parametersString):
    splitByObjects = parametersString[1:-1].split(')(') # Splits by objects(name:value,name:value,name:value;name:value,name:value,name:value)
    splitByParams = [param.split(',') for param in splitByObjects] # Splits by parameters (name:value,name:value,name:value)
    objectArray = []
    for paramSet in splitByParams:
        object = dict()
        for param in paramSet:
            splitByNameValue = param.split(':') # Splits between the name and value (name:value)
            object[splitByNameValue[0]] = splitByNameValue[1]
        objectArray += [object]
    print(objectArray)
    return objectArray

# WARNING! This doesn't actually give us total security. It only gives us obscurity.
def encrypt(sensitive_data):
    cipher = ARC4.new(socket.gethostname().encode('utf-8'))
    encoded = base64.b64encode(cipher.encrypt(sensitive_data.encode('utf-8')))
    return encoded

def decrypt(encoded_sensitive_data):
    cipher = ARC4.new(socket.gethostname().encode('utf-8'))
    decoded = cipher.decrypt(base64.b64decode(encoded_sensitive_data[2:-1]))
    return decoded.decode('utf-8')