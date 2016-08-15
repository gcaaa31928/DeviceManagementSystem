from rest_framework import serializers
from DeviceManagementSystemApp.models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ('id', 'name')

class DeviceSerializer(serializers.ModelSerializer):
    owner = StudentSerializer(read_only=True)
    class Meta:
        model = Devices
        fields = (
            'id',
            'name',
            'owner'
        )