from django.test import TestCase
from .models import Image, Profile
# Create your tests here.


class ImageTestClass(TestCase): 

    # Set up method
    def setUp(self):
        self.pic= Image(image = 'sky', Image_Name = 'Test', Image_Caption ='Test Caption', Likes ='Test Like', Comments='Test Comment')


    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.pic,Image))


    # Test Save Method
    def test_save_method(self):
        self.pic.save_image()
        images = Image.objects.all()
        self.assertTrue(len(editors) > 0)




        