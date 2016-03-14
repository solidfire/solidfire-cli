
class SolidFireRequestException(Exception):
    message = "An unknown exception occurred."

    def __init__(self, arg):
        self.msg = arg
