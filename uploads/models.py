from django.db import models

# Create your models here.
class Image(models.Model):
    
    Image_name = models.CharField(max_length =30) 
    Image_caption = models.CharField(max_length =30)
    Likes = models.CharField(max_length =10)
    Comments = models.CharField(max_length =100)
    Profile_pic = models.ForeignKey


class Profile(models.Model):
    Profile_photo =
    Bio = models.CharField(max_length = 500)
    
