from django.urls import path
from . import views
app_name = 'mystore'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('product/', views.product, name = 'product'),
    path('product_details/', views.product_details, name = 'product_details'),
    path('contact/', views.contact, name = 'contact'),
    path('login/', views.login, name = 'login'),
    path('register/', views.register, name = 'register'),
]