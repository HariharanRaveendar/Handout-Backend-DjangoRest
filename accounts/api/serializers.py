from rest_framework import serializers
from django.contrib.auth.models import User

class SignupSerilizers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password','email','first_name']


class SigninSerilizers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']
