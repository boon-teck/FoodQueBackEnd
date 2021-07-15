from comments.models import Comment
from rest_framework.decorators import api_view
from rest_framework.response import Response
from comments.serializers import CommentSerializer
from rest_framework import status

# Create your views here.
# @api_view(['GET'])
# def all_tasks(request):
#     tasks = Task.objects.all()
#     serializer = TaskSerializer(tasks, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def show_task(request, id):
#     task = Task.objects.get(pk=id)
#     serializer = TaskSerializer(task, many=False)
#     return Response(serializer.data)

@api_view(['POST'])
def create_comment(request, id):
    #request.data of the tasks(how do I pass in id ok im tired need to sleep)
    #then pass in comment ? how do I do that
    print('request', request.data["comment_content"])
    request.data['task'] = id
    serializer = CommentSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
    else: 
        return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.data)
    
""""
reference
def visitor_checkin_checkout(request):
    print(request.data["company"])
        # body_of_request = json.loads(request.body)
        try:
            # pass
            company = Company.objects.get(pk=request.data["company"])

        except Company.DoesNotExist:
            return Response(
                {"detail": "company in records"}, status=status.HTTP_403_FORBIDDEN
            )

        request.data["user"] = request.user.id
        company_visitor = CompanyVisitSerializer(data=request.data)

        if company_visitor.is_valid():
            company_visitor.save()

            # company.
            return Response({}, status=status.HTTP_200_OK)
        else:
            print(company_visitor.errors)
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
"""


# @api_view(['PUT'])
# def edit_task(request,messageid):
#     try:
#         task = Task.objects.get(pk=messageid)
#     except Task.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     serializer = TaskSerializer(task, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['DELETE'])
# def delete_task(request, messageid):
#     task = Task.objects.get(pk=messageid)
#     task.delete()
#     return Response("task deleted", status=status.HTTP_204_NO_CONTENT)