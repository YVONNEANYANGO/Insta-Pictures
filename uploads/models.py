from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    Profile = models.ImageField(upload_to = 'images/')
    User = models.CharField(max_length = 60)
    Bio = models.CharField(max_length = 500)
   

    # Methods

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self):
        self.update()

    def __str__(self):
        return self.User


class Image(models.Model):
    Image = models.ImageField(upload_to = 'images/')
    Image_Name = models.CharField(max_length =60) 
    Image_Caption = models.CharField(max_length =60)
    Likes = models.CharField(max_length =10)
    Comments = models.CharField(max_length =60)
    Profile = models.ForeignKey(Profile)
    pub_date = models.DateTimeField(auto_now_add=True)
    profile_image = models.ImageField(upload_to='profiles/')
    User = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)


class Comment(models.Model):
    name = models.CharField(max_length = 30)
    user = models.ForeignKey(User, null = True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)


    @classmethod
    def todays_photos(cls):
        today = dt.date.today()
        uploads = cls.objects.filter(pub_date__date = today)
        return uploads
    
    def save_image(self):
        self.save()

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length =30)
    email = models.EmailField()


    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.update()

    def __str__(self):
        return self.Image

    
    @classmethod
    def days_photos(cls,date):
        uploads = cls.objects.filter(pub_date__date = date)
        return uploads


    @classmethod
    def search_by_Profile(cls,search_profile):
        uploads = cls.objects.filter(user_name__icontains=search_profile)
        return images


