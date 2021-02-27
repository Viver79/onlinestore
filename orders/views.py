import json
from django.http import JsonResponse
from decimal import Decimal
from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.models import Cart



# Create your views here.

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                #OrderItem.objects.create(bike='bike')
                OrderItem.objects.create(order=order,
                                         bike=item['bike'],
                                         price=item['price'],
                                         quantity=item['quantity']
                                         )
            #Очищаем корзину
            cart.clear()

            return render(request, 'created.html', {'order':order})

    else:
        form = OrderCreateForm()

    return render(request, 'create.html', {'cart':cart, 'form':form})