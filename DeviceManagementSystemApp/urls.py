from django.conf.urls import url

from DeviceManagementSystemApp.api import devices
from DeviceManagementSystemApp.api import users

app_name = 'DeviceManagementSystemApp'
urlpatterns = [
    url(r'^devices', devices.devices, name='devices'),
    url(r'^user/ldap_login', users.ldap_login, name='ldap_login')
]
