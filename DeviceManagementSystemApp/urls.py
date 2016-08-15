from django.conf.urls import url

from DeviceManagementSystemApp.api import devices

app_name = 'DeviceManagementSystemApp'
urlpatterns = [
    url(r'^devices', devices.devices, name='devices')
]
