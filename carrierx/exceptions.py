class CxException(Exception):
    def __init__(self, message=None):
        super().__init__(message)
        self.message = message


class ApiMultipleFoundException(CxException):
    pass


class ApiNotFoundException(CxException):
    pass


class ApiPermissionException(CxException):
    pass


class ApiServerError(CxException):
    pass


class ApiValueError(CxException):
    pass
