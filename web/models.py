

from django.db import models
from versatileimagefield.fields import VersatileImageField,PPOIField
from tinymce.models import HTMLField

# Create your models here.
class Testimonial(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=335)
    designation=models.CharField(max_length=100)
    image = VersatileImageField('Image',upload_to='index/',ppoi_field='ppoi')
    ppoi = PPOIField('Image PPOI')

    def __str__(self):
        return self.name



class Brand(models.Model):
    title=models.CharField(max_length=225)
    image = VersatileImageField('Image',upload_to='index/',ppoi_field='ppoi')
    ppoi = PPOIField('Image PPOI')

    def __str__(self):
        return self.title



class Update(models.Model):
    title=models.CharField(max_length=225)
    summary=models.CharField(max_length=335)
    date=models.DateField()
    image = VersatileImageField('Image',upload_to='update/',ppoi_field='ppoi')
    ppoi = PPOIField('Image PPOI')
    content= HTMLField(blank=True, null=True)
    slug=models.SlugField(unique=True)

    def __str__(self):
        return self.title



class Gallery(models.Model):
    title=models.CharField(max_length=225)
    image = VersatileImageField('Image',upload_to='gallery/',ppoi_field='ppoi')
    ppoi = PPOIField('Image PPOI')

    def __str__(self):
        return self.title


class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField()
    message=HTMLField(blank=True, null=True)

    def __str__(self):
        return self.name
  

class Category(models.Model):
    title=models.CharField(max_length=225)
    slug=models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    title=models.CharField(max_length=225)
    description=models.CharField(max_length=500)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image = VersatileImageField('Image',upload_to='product/',ppoi_field='ppoi')
    ppoi = PPOIField('Image PPOI')
    is_popular=models.BooleanField(default=False)

    def __str__(self):
        return self.title




