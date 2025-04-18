from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Make sure RawMaterial is imported
from store.models import Product, Supplier, Buyer, Order, RawMaterial


@login_required(login_url='login')
def dashboard(request):
    total_product = Product.objects.count()
    total_supplier = Supplier.objects.count()
    total_buyer = Buyer.objects.count()
    total_order = Order.objects.count()
    # Add this line to count raw materials
    total_raw_materials = RawMaterial.objects.count()
    orders = Order.objects.all().order_by('-id')

    context = {
        'product': total_product,
        'supplier': total_supplier,
        'buyer': total_buyer,
        'order': total_order,
        # Pass the raw materials count to the template
        'raw_materials': total_raw_materials,
        'orders': orders
    }
    return render(request, 'dashboard.html', context)
