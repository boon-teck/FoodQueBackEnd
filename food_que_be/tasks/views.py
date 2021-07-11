from django.shortcuts import render
from tasks.models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tasks.serializers import TaskSerializer


@api_view(['GET'])
def all_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def show_task(request, id):
    task = Task.objects.get(pk=id)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)