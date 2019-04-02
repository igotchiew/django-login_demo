from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Category, Product


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm


class ProductAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'product_name', 'price']
    list_editable = ['price']
    list_filter = ['category_name']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)