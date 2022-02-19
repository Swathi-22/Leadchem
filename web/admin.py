from django.contrib import admin
from .models import Testimonial,Brand,Update,Gallery,Contact,Category,Product


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'image',)

@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'summary',)
    prepopulated_fields = {'slug':('title',)}


    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ( 'title',)
    prepopulated_fields = {'slug':('title',)}


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ( 'title',)
    


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'description',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'message',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'description',)
