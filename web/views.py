

from django.shortcuts import get_object_or_404, render

from web.models import Brand, Category, Contact, Gallery, Product, Testimonial, Update
from .forms import ContactForm

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
    context = {
        'product':product
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
    contact=Contact.objects.all()
    forms=ContactForm(request.POST or None)
    if request.method=='POST':
        if forms.is_valid():
            forms.save()
    context = {
        'contact':contact,
        'forms':forms

    }
    return render(request,'web/contact.html',context)