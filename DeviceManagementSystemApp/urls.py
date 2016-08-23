from django.conf.urls import url

from DeviceManagementSystemApp.api import devices
from DeviceManagementSystemApp.api import users

app_name = 'DeviceManagementSystemApp'
urlpatterns = [
    url(r'^devices', devices.devices, name='devices'),
    url(r'^device/check_in/(?P<token>[a-z|A-Z|0-9]+)', devices.check_in, name='check_in'),
    url(r'^device/check_out/(?P<token>[a-z|A-Z|0-9]+)', devices.check_out, name='check_out'),
    url(r'^device/(?P<id>[0-9]+)', devices.device, name='device'),
    url(r'^user/ldap_login', users.ldap_login, name='ldap_login')
]
