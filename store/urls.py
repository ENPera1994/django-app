from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('login/', views.loginArchitect, name='login'),
    # path('logout/', views.logoutArchitect, name='logout'),
    path('register/', views.registerArchitect, name='register'),
    path('product/<int:pk>', views.product, name='product'),
    path('products/', views.products, name='products'),
    path('fachadas/', views.fachadas, name='fachadas'),
    path('architects/', views.architects, name='architects'),
]