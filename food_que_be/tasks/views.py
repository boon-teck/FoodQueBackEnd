from tasks.models import Task
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from tasks.serializers import TaskSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

#user submitted tasks
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_tasks(request):
    print('test', request.user.id)
    tasks = Task.objects.filter(user=request.user)
    print(tasks)
    serializer = TaskSerializer(tasks, many=True)
    print(serializer)
    return Response(serializer.data)



@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def show_task(request, id):
    task = Task.objects.get(pk=id)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def create_task(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    else: 
        return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.data)
    

@api_view(['PUT'])
# @permission_classes([IsAuthenticated])
def edit_task(request,taskid):
    try:
        task = Task.objects.get(pk=taskid)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TaskSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def delete_task(request, taskid):
    task = Task.objects.get(pk=taskid)
    task.delete()
    return Response("task deleted", status=status.HTTP_204_NO_CONTENT)

