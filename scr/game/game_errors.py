# errorit pelin luvun erroreita varten

class CorruptedSaveFileError(Exception):
    def __init__(self, message):
        super(CorruptedSaveFileError, self).__init__(message)
        self.message = message

class CorruptedConfigureFileError(Exception):

    def __init__(self, message):
        super(CorruptedConfigureFileError, self).__init__(message)
        self.message = message