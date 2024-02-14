from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
    # service provider ---------------------------------------------------------------------------
    path('CreateService/', views.CreateService.as_view(), name='CreateService'),#create service
    path('ListService/', views.ListService.as_view(), name='ListService'),#List service
    path('UpdateService/<int:pk>/', views.UpdateService.as_view(), name='UpdateService'),
    path('DeleteService/<int:pk>/',views.DeleteService.as_view(),name='DeleteService'),
    path('ListRequests/<int:service_provider_id>/', views.ListRequests.as_view(), name='ListRequests'),
    path('UpdateRequest/<int:pk>/', views.UpdateRequest.as_view(), name='UpdateRequest'),


    # user ---------------------------------------------------------------------------------------


    path('register/', views.Register.as_view(), name='user-registration'),#registeration
    path('CreateRequest/<int:sr_id>/',views.CreateRequest.as_view(),name='CreateRequest'),
    path('createProfile/',views.createProfile.as_view(), name='profile'),
    path('ProfileView/', views.ProfileView.as_view(), name='ProfileView'),
    path('ListServiceProviders/<int:category_id>/<int:location_id>/', views.ListServiceProviders.as_view(), name='ListServiceProviders'),
    path('Createfeedback/<int:sr_id>/',views.CreateFeedback.as_view(),name='CreateFeedback'),
    path('ListFeedback/<int:service_id>/',views.ListFeedback.as_view(),name='ListFeedback'),
    path('Deletefeedback/<int:pk>/',views.Deletefeedback.as_view(),name='Deletefeedback'),
    path('ListmyRequests/',views.ListmyRequests.as_view(),name='ListmyRequests'),
    path('DeleteRequest/<int:pk>/',views.DeleteRequest.as_view(),name='DeleteRequest'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

