from typing import Collection
from django.shortcuts import render
from store.models import Product, Customer, Order, OrderItem, Collection, Cart, CartItem
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.db.models import Value, F, Func, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from tags.models import TaggedItem
from django.db import transaction
from django.core.mail import EmailMessage, BadHeaderError
from templated_mail.mail import BaseEmailMessage
from .tasks import notify_customers
# Create your views here.

def say_hello(request):
    
    notify_customers.delay('Hello')
    
    # try:
    #     message = BaseEmailMessage(
    #         template_name='emails/hello.html',
    #         context={'name': 'mosh'}
    #     )
    #     message.send(['jon@mosh.com'])
    # except BadHeaderError:  
    #     pass

    #counts the number of the specified field
    # result = OrderItem.objects.filter(product__id=1).aggregate(units=Sum('quantity'))
    # #number of orders placed by customer 1
    # result2 = Order.objects.filter(customer__id=1).aggregate(count=Count('id'))
    # #max min and average of the unit prices in collection 3
    # result3 = Product.objects.filter(collection__id=3).aggregate(min=Min('unit_price'), max=Max('unit_price'), avg=Avg('unit_price'))
    # #gets all the customers in the database that have the name andrew
    # query_set = Customer.objects.filter(first_name__icontains=('Andrew'))

    # full_names = Customer.objects.annotate(
    #     full_name=Concat('first_name', Value(' '), 'last_name')
    # )

    # count = Customer.objects.annotate(orders_count=Count('order'))

    # discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    # discount = Product.objects.annotate(discount_price=discounted_price)

    # #customers with their last order id
    # last_order = Customer.objects.annotate(last_order=Max('order__id'))

    # #collections and their product count
    # collection_count = Collection.objects.annotate(item_count=Count('product'))

    # #cutsomers with more than 5 orders
    # cust = Customer.objects.annotate(order_number=Count('order')).filter(order_number__gt=5)

    # #customers and the total amount they have spent
    # spent = Customer.objects.annotate(spent=Sum(F('order__orderitem__unit_price') * F('order__orderitem__quantity')))

    # #top 5 best selling products and their total sales
    # top_five = Product.objects.annotate(total_sales=Sum(F('orderitem__unit_price') * F('orderitem__quantity'))).order_by('-total_sales').values()[:5]

    # with transaction.atomic():
    #     order = Order()
    #     order.customer_id = 1
    #     order.save()

    #     item = OrderItem()
    #     item.order = order
    #     item.product_id = 1
    #     item.quantity = 1
    #     item.unit_price = 10

    #     item.save()

    return render(request, 'hello.html')

