from gettext import Catalog
from multiprocessing import context
from unicodedata import category
from django.shortcuts import render

from web.models import Brand, Category, Contact, Gallery, Product, Testimonial, Update

# Create your views here.
def index(request):
    testimonial=Testimonial.objects.all()
    brand=Brand.objects.all()
    context = {
        'testimonial':testimonial,
        'brand':brand

    }
    return render(request,'web/index.html',context)



def about(request):
    context = {

    }
    return render(request,'web/about.html',context)



def product(request):
    category=Category.objects.all()
    product=Product.objects.all()
    context = {
        'category':category,
        'product':product
    }
    return render(request,'web/product.html',context)



def blog(request):
    update=Update.objects.all()
    context = {
        'update':update

    }
    return render(request,'web/blog.html',context)



def blogDetails(request):
    update=Update.objects.all()
    context = {
        'update':update

    }
    return render(request,'web/blog-details.html',context)


def gallery(request):
    gallery=Gallery.objects.all()
    context = {
        'gallery':gallery

    }
    return render(request,'web/gallery.html',context)



def contact(request):
    contact=Contact.objects.all()
    context = {
        'contact':contact

    }
    return render(request,'web/contact.html',context)