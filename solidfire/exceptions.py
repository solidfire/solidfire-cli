class SolidFireUsageException(Exception):
    message = "A usage exception occurred"

    def __init__(self, arg):
        self.msg = arg

class SolidFireConnectionException(Exception):
    message = "A connection exception occurred"

    def __init__(self, arg):
        self.msg = arg

class SolidFireRequestException(Exception):
    message = "An unknown exception occurred."

    def __init__(self, arg):
        self.msg = arg
