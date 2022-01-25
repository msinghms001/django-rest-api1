from django.shortcuts import render,HttpResponse
from django.views.generic import CreateView
from rest_framework.viewsets import ModelViewSet
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# from rest_framework.authentication import (SessionAuthentication, 
#                                     BasicAuthentication, 
#                                     TokenAuthentication)
# from rest_framework import status
# from rest_framework.decorators import api_view,permission_classes
# from rest_framework.mixins import ListModelMixin,CreateModelMixin

from django.contrib.auth.models import User
from django.contrib.auth import login
from .import serializers

from rest_framework.views import APIView

from rest_framework.generics import ListAPIView,GenericAPIView

from rest_framework.response import Response

from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny,IsAuthenticated
import json
from rest_framework.authtoken.serializers import AuthTokenSerializer

# class ListAp(ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = serializers.SignupSer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.SignupSer

class TestApi(APIView):
    permission_classes = (IsAuthenticated, )
  
    def get(self, request):
        content = {'message': 'Hello, GeeksforGeeks'}
        return Response(content)

class RegisterAPI(GenericAPIView):
    serializer_class = serializers.RegisterSerializer   
    permission_classes=[AllowAny]

    def get(self,request):
        return Response("ok")

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # token=Token.objects.create(user=user)
        # print('token is ...',token,'and ',token.key)
        resp={
        "user":serializers.UserSerializer(user, context=self.get_serializer_context()).data,
        # "token": token.key
        }
        return Response(resp)


class Loginuser(GenericAPIView):
    permission_classes=[AllowAny]

    def get(self,request):
        resp={}
        resp['msg']='Not auth!'
        return Response(resp)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super().post(request, format=None)

        

    def post(self):
        pass




class Forgot(APIView):
    permission_classes = [AllowAny]

    def get(self,request):
        mail=request.GET.get('mail')
        return Response({
        
        'message':'reset mail sent! to '+mail
        
        })

class Reset(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        reqBody = json.loads(request.body)
        otp_code=reqBody['user_reset_hash']
        return Response({'message':'reset ok'})
