

from django.db import models
from versatileimagefield.fields import VersatileImageField,PPOIField
from tinymce.models import HTMLField

# Create your models here.
class Testimonial(models.Model):
    image = VersatileImageField('Image',upload_to='index/',ppoi_field='ppoi')
    ppoi = PPOIField('Image PPOI')
    title=models.CharField(max_length=225)
    description=models.CharField(max_length=335)
    name=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)

    def __str__(self):
        return self.title



class Brand(models.Model):
    image = VersatileImageField('Image',upload_to='index/',ppoi_field='ppoi')
    ppoi = PPOIField('Image PPOI')
    title=models.CharField(max_length=225)

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
    image = VersatileImageField('Image',upload_to='gallery/',ppoi_field='ppoi')
    ppoi = PPOIField('Image PPOI')
    title=models.CharField(max_length=225)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField()
    message=HTMLField(blank=True, null=True)

    def __str__(self):
        return self.title
  

class Category(models.Model):
    title=models.CharField(max_length=225)
    slug=models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    image = VersatileImageField('Image',upload_to='product/',ppoi_field='ppoi')
    ppoi = PPOIField('Image PPOI')
    title=models.CharField(max_length=225)
    description=models.CharField(max_length=500)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    is_popular=models.BooleanField(default=False)

    def __str__(self):
        return self.title




