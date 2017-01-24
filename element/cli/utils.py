from element.exceptions import *
import jsonpickle
import json as serializer

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
        objs_to_print = filter_objects_from_simple_keypaths(objs, filter_tree.split(','))
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
    filteredDict = dict()
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
    if type(nestedDict) is str:
        return nestedDict
    if nestedDict is None:
        return nestedDict

def get_result_as_tree(objs, depth=1, currentDepth=0, lastKey = ""):
    stringToReturn = ""
    if(currentDepth > depth):
        return "<to see more details, increase depth>\n"
    if(type(objs) is str or type(objs) is bool or type(objs) is int or objs is None):
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
        finalFilteredObjects[key] = filter_objects(dictionaryOfInterest[key], keyPaths[key])
    return finalFilteredObjects

def print_result_as_table(objs, keyPaths):
    filteredDictionary = filter_objects(objs, keyPaths)

def print_result_as_tree(objs, depth=1):
    print(get_result_as_tree(objs, depth))

def print_list(objs, fields, formatters={}, order_by=None):
    pt = prettytable.PrettyTable([f for f in fields], caching=False)
    pt.aligns = ['l' for f in fields]
    pt.max_width = 80
    if not objs:
        objs = []

    for o in objs:
        row = []
        for field in fields:
            if field == 'qos':
                # The QoS attribute is ridiculously long with the curve
                # data, which frankly isn't that useful for an end user, so
                # let's pop it off of the object here for display
                o['qos'].pop('curve', None)
            if field in formatters:
                row.append(formatters[field](o))
            else:
                field_name = field.replace(' ', '_')
                if type(o) == dict and field in o:
                    data = o[field]
                else:
                    data = getattr(o, field_name, '')
                row.append(data)
        pt.add_row(row)

    print(pt)
