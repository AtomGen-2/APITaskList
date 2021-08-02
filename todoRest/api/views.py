# from todoRest.api import serializers
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from api.serializers import TaskSerializer
from api.models import Task
from rest_framework import status
from rest_framework.parsers import JSONParser

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': 'task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/'
    }
    # safe = False is used to maintain that if non-dictionary type objects is passed, it should not throw an errror
    # Response vs JsonResponse: Response is providing us with the signature django rest viewframe, JsonResponse only returns the nasic reponse in line
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    # gets all the objects inside the Task model
    tasks = Task.objects.all()
    # serializes all the objects inside the Task model object list (tasks) due to many = True
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    # gets all the objects inside the Task model
    task = Task.objects.get(pk = pk)
    # serializes all the objects inside the Task model object list (tasks) due to many = True
    serializer = TaskSerializer(task)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    # serializes all the objects inside the Task model object list (tasks) due to many = True
    serializer = TaskSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def taskUpdate(request, pk):
    # gets all the objects inside the Task model
    task = Task.objects.get(pk = pk)
    # serializes all the objects inside the Task model object list (tasks) due to many = True
    serializer = TaskSerializer(instance = task, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def taskDelete(request, pk):
    # gets all the objects inside the Task model
    task = Task.objects.get(pk = pk)
    task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
