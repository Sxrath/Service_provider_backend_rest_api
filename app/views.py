from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from . import models
from . import serializers 
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken





# service Provider ------------------------------------------------

class Register(APIView):
    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({"status":403,'errors':serializer.errors,"message":'invalid data'})

        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        refresh = RefreshToken.for_user(user)

        return Response({"message": "Successfully registered!",   'refresh': str(refresh),
        'access': str(refresh.access_token,)}, status=status.HTTP_201_CREATED)



class CreateService(generics.CreateAPIView):
    serializer_class = serializers.CreateServiceSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ListService(generics.ListAPIView):
    serializer_class = serializers.ListServiceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        
        queryset = models.ServiceProvider.objects.filter(user=user)
        return queryset


        
class UpdateService(generics.UpdateAPIView):
    serializer_class = serializers.CreateServiceSerializer
    permission_classes = [IsAuthenticated]
    queryset= models.ServiceProvider.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DeleteService(generics.RetrieveDestroyAPIView):
    serializer_class = serializers.DeleteServiceSerializer
    permission_classes = [IsAuthenticated]
    queryset = models.ServiceProvider.objects.all()
    
    def destroy(self, request, *args, **kwargs):  
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Service deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

        
class ListRequests(generics.ListAPIView):
    serializer_class = serializers.RequestViewSerializer
    queryset = models.Requests.objects.all()

    def get_queryset(self):
        service_provider_id = self.kwargs.get('service_provider_id')
        service_provider = get_object_or_404(models.ServiceProvider, id=service_provider_id)
        return models.Requests.objects.filter(Service=service_provider)
    
class UpdateRequest(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.RequestUpdateSerializer
    permission_classes = [IsAuthenticated]
    queryset= models.Requests.objects.all()

class createProfile(generics.CreateAPIView):
    serializer_class = serializers.CreateUserProfileserializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProfileView(generics.RetrieveAPIView):
    serializer_class = serializers.CreateUserProfileserializer
    permission_classes=[IsAuthenticated]

    def get_object(self):
        profile_instance=get_object_or_404(models.UserProfile,user=self.request.user)
        return profile_instance


# User------------------- 
    

class ListServiceProviders(APIView):
    def get(self, request, category_id, location_id):  # Add 'request' parameter if needed
        category = get_object_or_404(models.Catergory, pk=category_id)
        location = get_object_or_404(models.Locations, pk=location_id)
        service_providers = models.ServiceProvider.objects.filter(Category=category, Location=location, approve=True)
        serializer = serializers.ServiceProviderSerializer(service_providers, many=True)
        return Response(serializer.data)


class CreateRequest(generics.CreateAPIView):
    serializer_class = serializers.CreateRequestSerializer
    queryset = models.Requests.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        service_id = self.kwargs.get("sr_id")
        service = get_object_or_404(models.ServiceProvider, id=service_id)
        user = self.request.user
        serializer.save(Service=service, User=user)


class CreateFeedback(generics.CreateAPIView):
    serializer_class=serializers.Feedbackserializer
    queryset = models.Feedback.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user=self.request.user
        sr_id=self.kwargs.get('sr_id')
        instance=get_object_or_404(models.ServiceProvider,id=sr_id)
        serializer.save(user=user,service=instance)
        return super().perform_create(serializer)

class ListFeedback(generics.ListAPIView):
    serializer_class = serializers.ListFeedbackSerializer
    queryset = models.Feedback.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        service_id = self.kwargs.get('service_id')
        return models.Feedback.objects.filter(service=service_id)

class Deletefeedback(generics.RetrieveDestroyAPIView):
    serializer_class=serializers.Deletefeedbackserializer
    permission_classes = [IsAuthenticated]
    queryset=models.Feedback.objects.all()

class ListmyRequests(generics.ListAPIView):
    serializer_class=serializers.MyRequests
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        queryset=models.Requests.objects.filter(User=user)
        return queryset
    
class DeleteRequest(generics.DestroyAPIView):
    serializer_class = serializers.DeleteRequestserializer
    permission_classes = [IsAuthenticated]
    queryset = models.Requests.objects.all()
