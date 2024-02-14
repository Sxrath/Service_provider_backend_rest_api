from django.contrib import admin
from .models import Catergory,ServiceProvider,Requests,UserProfile,Locations,Feedback
# Register your models here.


# admin.site.register(CustomUser)
admin.site.register(Catergory)
admin.site.register(ServiceProvider)
admin.site.register(Requests)
admin.site.register(UserProfile)
admin.site.register(Locations)
admin.site.register(Feedback)