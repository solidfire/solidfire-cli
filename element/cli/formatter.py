import six
import strutils
import prettytable


def print_dict(d, property="Property"):
    pt = prettytable.PrettyTable([property, 'Value'], caching=False)
    pt.aligns = ['l', 'l']
    [pt.add_row(list(r)) for r in six.iteritems(d)]
    print(strutils.safe_encode(pt.get_string(sortby=property)))


def print_list(objs, fields, formatters={}, order_by=None):
    pt = prettytable.PrettyTable([f for f in fields], caching=False)
    pt.aligns = ['l' for f in fields]
    pt.max_width = 20

    for o in objs:
        row = []
        for field in fields:
            if field == 'qos':
                # The QoS attribute is ridiculously long with the curve
                # data, which frankly isn't that useful for an end user, so
                # let's pop it off of the object here for display
                getattr(o, field).pop('curve', None)
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
