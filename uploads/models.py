from django.db import models

# Create your models here.
class Profile(models.Model):
    Profile = models.ImageField(upload_to = 'images/')
    Bio = models.CharField(max_length = 500)

    # Methods

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self):
        self.update()

    def __str__(self):
        return self.name


class Image(models.Model):
    Image = models.ImageField(upload_to = 'images/')
    Image_Name = models.CharField(max_length =60) 
    Image_Caption = models.CharField(max_length =60)
    Likes = models.CharField(max_length =10)
    Comments = models.CharField(max_length =60)
    Profile = models.ForeignKey(Profile)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.update()

    def __str__(self):
        return self.name


# class Profile(models.Model):
#     Profile = models.ImageField(upload_to = 'images/')
#     Bio = models.CharField(max_length = 500)

#     # Methods

#     def save_profile(self):
#         self.save()

#     def delete_profile(self):
#         self.delete()

#     def update_profile(self):
#         self.update()

#     def __str__(self):
#         return self.name
    
