# blog_app/views.py

import razorpay
from django.conf import settings
from django.shortcuts import render

def payment_page(request):
    amount = 9900  # Rs.99 in paise
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    
    payment = client.order.create({
        'amount': amount,
        'currency': 'INR',
        'payment_capture': '1'
    })

    context = {
        'amount': amount,
        'api_key': settings.RAZORPAY_KEY_ID,
        'order_id': payment['id'],
    }

    return render(request, 'payment.html', context)


def payment_success(request):
    return render(request, 'success.html')
