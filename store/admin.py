from operator import concat
from django.contrib import admin, messages
from . import models
from django.utils.html import format_html, urlencode
from django.db.models.aggregates import Count
from django.urls import reverse
# Register your models here.

class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'
    
    def lookups(self, request, model_admin):
        return [
            ('<10','Low')
        ]
    def queryset(self, request, queryset):
        if self.value() == '<10': 
            return queryset.filter(inventory__lt=10)



@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['collection']
    prepopulated_fields = {
        'slug': ['title']
    }
    actions = ['clear_inventory']
    list_display = ['title', 'unit_price', 'inventory_status', 'collection_title', 'number_of_orders']
    list_editable = ['unit_price']
    list_filter = ['collection', 'last_update', InventoryFilter]
    ordering = ['title']
    list_per_page = 10
    list_select_related = ['collection']
    search_fields = ['OrderItemInline']

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'
    @admin.display(ordering='number_of_orders')
    def number_of_orders(self, product):
        return product.number_of_orders

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(number_of_orders=Count('orderitem'))
    
    @admin.action(description='Clear Inventory')
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request,
            f'{updated_count} products were successfully updated.',
        )

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', 'orders']
    list_editable = ['membership']
    list_per_page = 10
    list_select_related = ['user']
    ordering = ['user__first_name', 'user__last_name']
    search_fields= ['first_name__istartswith', 'last_name__istartswith']

    @admin.display(ordering='orders')
    def orders(self, customer):
        url = (
            reverse('admin:store_order_changelist')
            + '?'
            +urlencode({
                'customer_id': str(customer.id)
            })
        )
        return format_html('<a href={}>{}</a>', url, customer.orders)
        

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(orders=Count('order'))

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']
    ordering = ['title']
    search_fields = ['title']

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        url = (
            reverse('admin:store_product_changelist')
             + '?'
             + urlencode({
                'collection_id': str(collection.id)
             })
             )
        return format_html('<a href="{}"> {}</a>', url,  collection.products_count)
        
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(products_count=Count('products'))

class OrderItemInline(admin.TabularInline):
    autocomplete_fields = ['product']
    model = models.OrderItem
    extra = 0
    min_num = 1


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']
    inlines = [OrderItemInline]
    list_display = ['id', 'placed_at', 'customer']
