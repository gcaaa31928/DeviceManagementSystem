from rest_framework.exceptions import APIException

class NoneExistsException(APIException):
    status_code = 400
    default_detail = 'none exists object'

