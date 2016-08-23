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
            'owner',
            'check_in_date_time',
            'used_for',
            'type',
            'issues',
            'token'
        )
        read_only_fields = (
            'id',
        )
