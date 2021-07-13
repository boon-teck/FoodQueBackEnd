from rest_framework.decorators import api_view
from rest_framework.response import Response
from tasks.serializers import TaskSerializer
from rest_framework import status, exceptions
from accounts.models import User
from accounts.serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken



@api_view(['POST'])
def register_user_api(request):
    user = UserSerializer(data=request.data)
    if user.is_valid():
        user.save()
        return Response("User registered", status=status.HTTP_201_CREATED)
    else:
        return Response({"details": dict(user.errors)}, status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
def login_user_api(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        raise exceptions.AuthenticationFailed

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise exceptions.AuthenticationFailed("user not found")

    # if user is None:
    #     raise exceptions.AuthenticationFailed("user not found")
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed("password is not a match")

    refresh = RefreshToken.for_user(user)
 

    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    })  