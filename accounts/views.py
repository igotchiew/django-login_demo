from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views import generic
from django.http import Http404
from django.template import loader
from .forms import CustomUserCreationForm
from .models import Category, Product


class HomePageView(TemplateView):
    template_name = 'home.html'


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


# index view in tutorial
def category(request):
    category_list = Category.objects.all()
    context = {
        'category_list': category_list,
    }
    return render(request, 'category.html', context)


# detail view in tutorial
def product(request, category_name):
    try:
        item = Product.objects.get(category_name=category_name)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request, 'product.html', {'item': item})