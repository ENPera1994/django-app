from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('product/<int:pk>', views.product, name='product'),
    path('products/', views.products, name='products'),
    path('fachadas/', views.fachadas, name='fachadas'),
    path('architects/', views.architects, name='architects'),
]