import uuid
from datetime import datetime

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from DeviceManagementSystemApp.models import Students, Devices
from DeviceManagementSystemApp.serializer import DeviceSerializer
from DeviceManagementSystemApp.utils.errors import NoneExistsException
from DeviceManagementSystemApp.views import JSONResponse


def get_student(meta):
    if 'HTTP_ACCESS_TOKEN' not in meta:
        return None
    access_token = meta.get('HTTP_ACCESS_TOKEN')
    results = Students.objects.filter(access_token=access_token)
    if results.exists():
        return results[0]
    raise NoneExistsException

def retrieve_data(data):
    id = data.get('id', None)
    name = data.get('name', None)
    used_for = data.get('user_for', None)
    type = data.get('type', None)
    issues = data.get('issues', None)
    return id, name, used_for, type, issues

@api_view(['POST', 'GET', 'POST', 'DELETE'])
def devices(request):
    student = get_student(request.META)
    if request.method == 'GET':
        return list(request)
    elif request.method == 'POST':
        return add(request, student)
    elif request.method == 'DELETE':
        return delete_all(request)
    return JSONResponse(None , status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def device(request, id):
    student = get_student(request.META)
    device = Devices.objects.get(id=id)
    if request.method == 'GET':
        return show(request, student, device)
    elif request.method == 'DELETE':
        return delete(request, student, device)

    return JSONResponse(None, status=status.HTTP_400_BAD_REQUEST)


def list(request):
    devices = Devices.objects.all()
    serializer = DeviceSerializer(devices, many=True)
    return JSONResponse(serializer.data, status=200)

def add(request, student):
    if not student.manager:
        return JSONResponse('forbidden', status=status.HTTP_403_FORBIDDEN)
    id, name, used_for, type, issues = retrieve_data(request.data)
    token = str(uuid.uuid1()).replace('-', '')
    device = Devices(
        name=name,
        used_for=used_for,
        type=type,
        issues=issues,
        token=token
    )
    device.save()
    serializer = DeviceSerializer(device)
    return JSONResponse(serializer.data, status=200)

def delete(request, student, device):
    if student.manager:
        device.delete()
        return JSONResponse('success', status=200)
    return JSONResponse('forbidden', status=status.HTTP_403_FORBIDDEN)

def show(request, student, device):
    serializer = DeviceSerializer(device)
    return JSONResponse(serializer.data, status=200)

def delete_all(request):
    pass

def check_in(request, token):
    student = get_student(request.META)
    device = Devices.objects.get(token=token)
    if device.owner:
        return JSONResponse('already had owner', status=status.HTTP_400_BAD_REQUEST)
    device.owner = student
    device.check_in_date_time = datetime.now()
    device.save()
    return JSONResponse('success', status=status.HTTP_200_OK)

def check_out(request, token):
    student = get_student(request.META)
    if not student.manager:
       return JSONResponse('forbidden', status=status.HTTP_403_FORBIDDEN)
    device = Devices.objects.get(token=token)
    if not device.owner:
        return JSONResponse('no owner with this device', status=status.HTTP_400_BAD_REQUEST)
    device.owner = None
    device.save()
    return JSONResponse('success', status=status.HTTP_200_OK)
