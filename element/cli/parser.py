from element import exceptions
def parse_array(input_string):
    # The base case is that it is None:
    if(input_string == '' or input_string == 'null' or input_string is None):
        return None
    # If it is surrounded by brackets, we just remove the brackets:
    if(input_string[0] == '[' and input_string[-1] == ']'):
        input_string = input_string[1:-1]
        # When we want an empty array.
        if input_string == '':
            return []

    # First, split the input string on ','
    array = str(input_string).split(',')
    return array