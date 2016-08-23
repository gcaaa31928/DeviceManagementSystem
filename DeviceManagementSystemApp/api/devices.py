import uuid
from datetime import datetime

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from DeviceManagementSystemApp.models import Students, Devices
from DeviceManagementSystemApp.serializer import DeviceSerializer
from DeviceManagementSystemApp.views import JSONResponse


def get_student(meta):
    if 'HTTP_ACCESS_TOKEN' not in meta:
        return None
    access_token = meta.get('HTTP_ACCESS_TOKEN')
    results = Students.objects.filter(access_token=access_token)
    if results.exists():
        return results[0]
    else:
        return None


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
        list(request)
    elif request.method == 'POST':
        add(request, student)
    elif request.method == 'DELETE':
        delete_all(request)

    return Response(None , status=status.HTTP_200_OK)

@api_view(['GET', 'DELETE'])
def device(request):
    student = get_student(request.META)


def list(request):
    devices = Devices.objects.all()
    serializer = DeviceSerializer(devices, many=True)
    return JSONResponse(serializer.data, status=200)

def add(request, owner):
    id, name, used_for, type, issues = retrieve_data(request.data)
    token = str(uuid.uuid1()).replace('-', '')
    device = Devices(
        id=id,
        name=name,
        owner=owner,
        used_for=used_for,
        type=type,
        issues=issues,
        token=token
    )
    device.save()

def show(request):
    pass

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
