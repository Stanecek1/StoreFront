from django.shortcuts import render
from store.models import Product, Customer, Order, OrderItem
from django.db.models.aggregates import Count, Max, Min, Avg, Sum

# Create your views here.
def say_hello(request):
    #counts the number of the specified field
    result = OrderItem.objects.filter(product__id=1).aggregate(units=Sum('quantity'))
    #number of orders placed by customer 1
    result2 = Order.objects.filter(customer__id=1).aggregate(count=Count('id'))
    #max min and average of the unit prices in collection 3
    result3 = Product.objects.filter(collection__id=3).aggregate(min=Min('unit_price'), max=Max('unit_price'), avg=Avg('unit_price'))
    #gets all the customers in the database that have the name andrew
    query_set = Customer.objects.filter(first_name__icontains=('Andrew'))
    return render(request, 'hello.html', {'andrews': list(query_set), 'result': result3})

