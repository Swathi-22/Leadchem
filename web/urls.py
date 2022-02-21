from django.urls import path

from . import views

app_name='web'

urlpatterns = [
    path('', views.index,name='index'),
    path('about/', views.about,name='about'),
    path('product/', views.product,name='product'),
    path('category/<slug:slug>/', views.category,name='category'),
    path('gallery/', views.gallery,name='gallery'),
    path('blog/', views.blog,name='blog'),
    path('blog-details/<str:slug>/', views.blogDetails,name='blogDetails'),
    path('contact/', views.contact,name='contact'),
]