from django.urls import path
from . import views
from .views import home_redirect

urlpatterns = [
    path('', home_redirect),
    path('subscribe/', views.subscription_page, name='subscription'),
    path('paymentpage/', views.payment_page, name='paymentpage')
]
from django.urls import path

