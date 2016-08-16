import uuid
from datetime import datetime

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from DeviceManagementSystemApp.models import Students, Devices


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
    check_in_date_time = datetime.now()
    used_for = data.get('user_for', None)
    type = data.get('type', None)
    issues = data.get('issues', None)
    return id, name, check_in_date_time, used_for, type, issues

@api_view(['POST', 'GET', 'POST', 'DELETE'])
def devices(request):
    student = get_student(request.META)
    # if student is None or not student.manager:
    #     return Response("Just forbidden", status=status.HTTP_403_FORBIDDEN)
    if request.method == 'GET':
        list(request)
    elif request.method == 'POST':
        add(request)
    elif request.method == 'DELETE':
        delete_all(request)

    return Response(None , status=status.HTTP_200_OK)

def list(request):
    pass

def add(request, owner):
    id, name, check_in_date_time, used_for, type, issues = retrieve_data(request.data)
    token = str(uuid.uuid1()).replace('-', '')
    device = Devices(
        id=id,
        name=name,
        owner=owner,
        check_in_date_time=check_in_date_time,
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

def check_out(request, student):
    pass