from rest_framework import serializers
from .models import ServiceProvider,Requests,UserProfile,Feedback
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','email']

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class CreateServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProvider
        fields=['Catergory','Shop_name','Location','Description'] 
        read_only_fields = ['user']  

class ListServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProvider
        fields = '__all__'


class DeleteServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=ServiceProvider
        fields=[]
        

class CreateRequestSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Requests
        fields = ['datetime','description']
        
class RequestViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requests
        fields = ['User','datetime','description']

class RequestUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requests
        fields = ['pending','accept','decline']

class MyRequests(serializers.ModelSerializer):
    class Meta:
        model = Requests
        fields = ['datetime','description','pending','accept','decline']
       
class DeleteRequestserializer(serializers.ModelSerializer):
    class Meta:
        model=Requests
        fields=[]

class CreateUserProfileserializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields=['first_name','last_name','image']

    
class ListService_Providersserializer(serializers.ModelSerializer):
    class Meta:
        model=ServiceProvider
        fields='__all__'

class Feedbackserializer(serializers.ModelSerializer):
    class Meta:
        model=Feedback
        fields=['feedback','rating']

class ListFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['feedback','rating','user']


class Deletefeedbackserializer(serializers.ModelSerializer):
    class Meta:
        model=Feedback
        fields=[]
class ServiceProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model=ServiceProvider
        fields=['user','Category','Shop_name','Location','Description']