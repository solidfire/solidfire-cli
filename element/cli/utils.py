import prettytable

import six


def print_dict(d, property="Property"):
    pt = prettytable.PrettyTable([property, 'Value'], caching=False)
    pt.aligns = ['l', 'l']
    [pt.add_row(list(r)) for r in six.iteritems(d)]
    print(pt.get_string(sortby=property))


def kv_string_to_dict(kv_string):
    new_dict = {}
    items = kv_string.split(',')
    for item in items:
        kvs = item.split('=')
        new_dict[kvs[0]] = kvs[1]

def print_result(objs, depth=None, fields=None, json=False):
    # If a depth is provided, we print it as a tree:
    if depth is not None:
        print_result_as_tree(objs, depth)
        return

    # If json is true, we print it as json:
    if json == True:
        print_result_as_json(objs)

    # If fields are provided, we print it as a table
    if fields is not None:
        print_result(objs)

def print_result_as_json(objs):
    print(json.dumps(json.loads(jsonpickle.encode(ListAccountsResult)),indent=4))

def get_result_as_tree(objs, depth=1, currentDepth=0, lastKey = ""):
    stringToReturn = ""
    if(currentDepth > depth):
        return "<to see more details, increase depth>\n"
    if(type(objs) is str or type(objs) is bool or type(objs) is int):
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
