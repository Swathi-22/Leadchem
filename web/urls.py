from django.urls import path

from . import views

app_name='web'

urlpatterns = [
    path('', views.index,name='index'),
    path('about/', views.about,name='about'),
    path('product/', views.product,name='product'),
    path('product-detail/', views.productDetails,name='productDetails'),
    path('gallery/', views.gallery,name='gallery'),
    path('blog/', views.blog,name='blog'),
    path('blog-detail/', views.blogDetails,name='blogDetails'),
    path('contact/', views.contact,name='contact'),
]