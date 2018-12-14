from django.db import models

# Create your models here.
class Image(models.Model):
    Image = models.ImageField(upload_to = 'images/')
    Image_Name = models.CharField(max_length =60) 
    Image_Caption = models.CharField(max_length =30)
    Likes = models.CharField(max_length =10)
    Comments = models.CharField(max_length =100)
    Profile_Pic = models.ForeignKey(Profile_Pic)


class Profile(models.Model):
    Profile_photo = models.ImageField(upload_to = 'images/')
    Bio = models.CharField(max_length = 500)

    # Methods

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self):
        self.update()

    def __str__(self):
        return self.profile
    
