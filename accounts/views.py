from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from .models import Category, Product


class HomePageView(TemplateView):
    template_name = 'home.html'


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def category(request):
    category_list = Category.objects.all()
    context = {
        'category_list': category_list,
    }
    return render(request, 'category.html', context)


def product(request, category_name):
    product_list = Product.objects.filter(category_name=category_name)
    context = {
        'product_list': product_list,
    }
    return render(request, 'product.html', context)