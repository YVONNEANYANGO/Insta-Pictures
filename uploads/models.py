from django.db import models
import datetime as dt

# Create your models here.
class Profile(models.Model):
    Profile = models.ImageField(upload_to = 'images/')
    User_Name = models.CharField(max_length = 60)
    Bio = models.CharField(max_length = 500)

    # Methods

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self):
        self.update()

    def __str__(self):
        return self.User_Name


class Image(models.Model):
    Image = models.ImageField(upload_to = 'images/')
    Image_Name = models.CharField(max_length =60) 
    Image_Caption = models.CharField(max_length =60)
    Likes = models.CharField(max_length =10)
    Comments = models.CharField(max_length =60)
    Profile = models.ForeignKey(Profile)
    pub_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def todays_photos(cls):
        today = dt.date.today()
        uploads = cls.objects.filter(pub_date__date = today)
        return uploads

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
        return self.Image_Name

    
    @classmethod
    def days_photos(cls,date):
        uploads = cls.objects.filter(pub_date__date = date)
        return uploads


    @classmethod
    def search_by_Profile_User_Name(cls,search_term):
        uploads = cls.objects.filter(user_name__icontains=search_term)
        return images


