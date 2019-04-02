from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('category/', views.category, name='category'),
    path('category/<category_name>', views.product, name='products'),
]