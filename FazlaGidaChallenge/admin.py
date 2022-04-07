from django.contrib import admin

from .models import Category, Product, Profile, Store

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(Store)
