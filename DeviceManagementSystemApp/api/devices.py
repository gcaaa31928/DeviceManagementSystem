from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from DeviceManagementSystemApp.models import Students




def get_student(meta):
    if 'HTTP_ACCESS_TOKEN' not in meta:
        return None
    access_token = meta.get('HTTP_ACCESS_TOKEN')
    results = Students.objects.filter(access_token=access_token)
    if results.exists():
        return results[0]
    else:
        return None

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

def add(request):
    request_data = request.data
    print(request_data)

def show(request):
    pass

def delete_all(request):
    pass

def check_out(request, student):
    pass