from django.contrib import admin

from .models import (
    Supplier,
    Buyer,
    Season,
    Drop,
    Product,
    Order,
    Delivery,
    RawMaterial,
    ProductRawMaterial,
)


class RawMaterialAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ['name', 'quantity', 'unit', 'created_at']
    search_fields = ['name']  # Add search functionality by name
    list_filter = ['unit']  # Add filtering by unit


class ProductRawMaterialAdmin(admin.ModelAdmin):
    list_display = ['product', 'raw_material', 'quantity_used']
    search_fields = ['product__name', 'raw_material__name']
    list_filter = ['product']


class SupplierAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'address', 'created_date']


class BuyerAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'address', 'created_date']


admin.site.register(RawMaterial, RawMaterialAdmin)
admin.site.register(ProductRawMaterial, ProductRawMaterialAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Buyer, BuyerAdmin)
admin.site.register(Season)
admin.site.register(Drop)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Delivery)
