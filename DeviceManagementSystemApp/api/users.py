import uuid

import ldap
from rest_framework.decorators import api_view

from DeviceManagementSystem import settings
from DeviceManagementSystemApp.models import Students
from DeviceManagementSystemApp.views import JSONResponse
from common.ldap_adapter import LDAPAdapter


@api_view(['POST'])
def ldap_login(request):
    data = request.data
    username = data.get('username', None)
    password = data.get('password', None)
    ldap_adapter = LDAPAdapter(username, password)
    if ldap_adapter.try_login():
        uid, name, mail = ldap_adapter.get_result()
        student = Students.objects.get_or_create(
            id=uid,
            name=name,
            mail=mail,
            manager=False
        )
        student.access_token = str(uuid.uuid1()).replace('-', '')
        student.save()
        return JSONResponse(student.access_token, status=200)
    else:
        return JSONResponse(None, status=403)
