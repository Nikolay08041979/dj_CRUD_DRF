from django.contrib import admin

from logistic.models import Product, Stock, StockProduct


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description"]
    list_filter = ["title"]


# @admin.register(Stock)
# class StockAdmin(admin.ModelAdmin):
#     list_display = ["id", "address", "product"]
#     list_filter = ["address"]

@admin.register(StockProduct)
class StockProductAdmin(admin.ModelAdmin):
    list_display = ["id", "stock", "product", "quantity", "price"]
    list_filter = ["stock"]
# Register your models here.
