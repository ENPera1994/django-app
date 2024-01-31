from django.urls import path
from . import views

urlpatterns = [
    path('', views.cartSummary, name='cartSummary'),
    path('add/', views.cartAdd, name='cartAdd'),
    path('delete/', views.cartDelete, name='cartDelete'),
    #path('procesar_pago/', views.procesar_pago, name='procesar_pago_mp.html'),
]