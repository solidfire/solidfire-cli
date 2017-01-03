def parse_array(input_string):
    # The base case is that it is None:
    if(input_string == '' or input_string is None):
        return None

    # First, split the input string on ','
    array = input_string.split(',')
    return array