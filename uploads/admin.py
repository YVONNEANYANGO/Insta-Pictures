from django.contrib import admin
from .models import Image, Profile

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('Profile') 

# Register your models here.
admin.site.register(Image)
admin.site.register(Profile)
