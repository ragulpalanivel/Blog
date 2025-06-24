from django.shortcuts import render
from django.shortcuts import redirect
from . import views
def subscription_page(request):
    return render(request, 'subscription.html')

def home_redirect(request):
    return redirect('subscription')
# blog_app/views.py


def payment_page(request):
    return render(request, 'paymentpage.html')  # Template name
