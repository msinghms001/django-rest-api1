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
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.core import mail
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
        resp={
            'message':'user created!'
        # "user":serializers.UserSerializer(user, context=self.get_serializer_context()).data,
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

class UpdatePass(APIView):
    def post(self,request,format=None):
        username=request.data.get('username')
        new_pass=request.data.get('new_pass')
        resp={}
        try:
            user=User.objects.get(username=username)
            user.set_password(new_pass)
            user.save()
            resp['message']='password updated successfully'
        except:
            resp['message']='problem updating password'
        
        return Response(resp)

        

class Forgot(APIView):
    permission_classes = [AllowAny]

    def get(self,request):
        mail=request.GET.get('mail')
        
        obj=User.objects.filter(email=mail)
        resp={}
        if obj.exists():
            try:
                token=Token.objects.create(user=obj[0])
                subject, from_email, to = 'Your Token', 'hpathomepc@gmail.com', mail
                text_content = 'This is an week message.'
                html_content = '<p>Your password reset code is</p>'
                html_content+=f'<br/><i> {token.key}</i>'
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()               
                resp['message']='reset mail sent! to '+mail

            except Exception as e:
                resp['message']='possibly token was already created or failed with reason:'+str(e) 
           
        else:
            resp['message']='mail was NOT sent'

        return Response(resp)

class Reset(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        otp_token=request.data.get('otp_token')
        new_pass=request.data.get('new_pass')
        
        resp={}
        try:
            dbTok=Token.objects.filter(key=otp_token)
            if dbTok.exists():
                user=dbTok[0].user
                user.set_password(new_pass)
                user.save()
                dbTok[0].delete()
                resp['message']='deleted success'
            
            else:
                resp['message']='no such token or user'


        except:
            resp['message']='wrong otp input'
        return Response(resp)
