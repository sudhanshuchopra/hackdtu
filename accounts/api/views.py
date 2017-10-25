from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import JsonResponse
from .serializers import (
    CsrfExemptSessionAuthentication,


    UserLoginSerializer,UserDetSerializer
)
from accounts.models import MyUser



# custom user login
class UserLoginAPI(APIView):
    permission_classes =[AllowAny]
    serializer_class = UserLoginSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        user=MyUser.objects.filter(adhaar_card=data["adhaar_card"])[0]
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            new_data["status"] = "Logi sucessfully"
            auth_login(request,user)
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    def get_object(self,adhaar_card=None):
        try:
            return MyUser.objects.get(adhaar_card=adhaar_card)
        except MyUser.DoesNotExist:
            raise Http404

    def get(self, request, adhaar_card, format=None):
        my_user = self.get_object(adhaar_card)
        serializer = UserDetSerializer(my_user)
        return Response(serializer.data)
        


