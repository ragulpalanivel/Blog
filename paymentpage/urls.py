# blog_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('pay/', views.payment_page, name='payment'),
    path('payment-success/', views.payment_success, name='payment_success'),
]
