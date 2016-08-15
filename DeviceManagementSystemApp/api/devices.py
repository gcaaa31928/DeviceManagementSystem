from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


def get_student(meta):
    if 'HTTP_ACCESS_TOKEN' not in meta:
        return None
    access_token = meta.get('HTTP_ACCESS_TOKEN')



@api_view(['POST', 'GET', 'POST', 'DELETE'])
def devices(request):
    get_student(request.META)
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
    pass

def show(request):
    pass

def delete_all(request):
    pass