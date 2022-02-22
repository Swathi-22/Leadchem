from django.shortcuts import get_object_or_404, render,HttpResponse
from django.http import JsonResponse
from web.models import Brand, Category, Gallery, Product, Testimonial, Update
from .forms import ContactForm
import json


def index(request):
    testimonial=Testimonial.objects.all()
    brand=Brand.objects.all()
    product=Product.objects.filter(is_popular=True)
    context = {
        'testimonial':testimonial,
        'brand':brand,
        'product':product
    }
    return render(request,'web/index.html',context)


def about(request):
    context = {

    }
    return render(request,'web/about.html',context)


def product(request):
    category=Category.objects.all()
    product=Product.objects.all()
    brands=Brand.objects.all()
    context = {
        'category':category,
        'product':product,
        'brands':brands
    }
    return render(request,'web/product.html',context)


def category(request,slug):
    category=Category.objects.get(slug=slug)
    product=Product.objects.filter(category=category)
    brands=Brand.objects.all()
    context = {
        'product':product,
        'brands':brands

    }
    return render(request,'web/product.html',context)


def blog(request):
    update=Update.objects.all()
    context = {
        'update':update

    }
    return render(request,'web/blog.html',context)


def blogDetails(request,slug):
    update=get_object_or_404(Update,slug=slug)
    # k= Update.objects.get(slug=slug)
    updates_deatails=Update.objects.exclude(pk=update.pk)[:5]
    context = {
        'update':update,
        'updates_deatails':updates_deatails
    }
    return render(request,'web/blog-details.html',context)


def gallery(request):
    gallery=Gallery.objects.all()
    context = {
        'gallery':gallery
    }
    return render(request,'web/gallery.html',context)


def contact(request):
    forms = ContactForm(request.POST or None)
    if request.method == 'POST':
        if forms.is_valid():
            data = forms.save(commit=False)
            data.referral = "web"
            data.save()
            response_data = {
                "status" : "true",
                "title" : "Successfully Submitted",
                "message" : "Message successfully submitted"
            }
        else:
            print (forms.errors)
            response_data = {
                "status" : "false",
                "title" : "Forms validation error",
                "message" : repr(forms.errors)
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        context = {
        "is_contact" : True,
        "forms" : forms,
        }
        return render(request,'web/contact.html',context)

