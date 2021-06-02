from rest_framework.decorators import api_view,authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .serializers import SignupSerilizers,SigninSerilizers
from rest_framework import status
from django.contrib.auth.models import User,auth

@api_view(["POST"])
def Signin(request):
    if request.method == 'POST':
        serializer = SigninSerilizers(data=request.data)
        if serializer.is_valid():
            username=serializer.data['username']
            password=serializer.data['password']
            print(username,password)
        user = auth.authenticate(request,username=serializer.data['username'], password=serializer.data['password'])
        print(user)
        if user is not None:
            print("user")
            res={}
            data= User.objects.filter(username=serializer.data['username'])
            for x in data:
                res['first_name']=x.first_name
                res['email']=x.email
                res['mobilenumber']=x.username
            return Response(res)
        else:
            print(serializer.errors)
            return Response("Invalid Creditinals")

@api_view(["POST","GET"])
def Signup(request):
    if request.method == 'POST':
        serializer=SignupSerilizers(data=request.data)
        if serializer.is_valid():
            username=serializer.data['username']
            password=serializer.data['password']
            email=serializer.data['email']
            first_name=serializer.data['first_name']
            user = User.objects.create_user(
                    first_name=first_name,
                    username=username,
                    email=email,
                    password=password
                )
            user.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == 'GET':
        user = User.objects.all()
        serializer = SignupSerilizers(user, many=True)
        return Response(serializer.data)

