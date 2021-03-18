from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    #price_from_form = float(request.POST["price"])
#forma diferente de obtener el precio
    produc_id=int(request.POST["producto_id"])
    producto = Product.objects.get(id=produc_id)
    price=producto.price

    total_charge = quantity_from_form * price
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)


    return redirect('/success')
    #return render(request, "store/checkout.html", context)

def success(request):
    order_all = Order.objects.all()
    gasto_total = 0
    for pedido in order_all:
        gasto_total += pedido.total_price

    item_all = 0
    for items in order_all:
        item_all += items.quantity_ordered


    orden = Order.objects.last()
    context = {
        'last_orden': orden,
        'item_all':item_all,
        'gasto_total': gasto_total,
    }
    return render(request, "store/checkout.html", context)
