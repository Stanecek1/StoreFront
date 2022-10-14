from django.urls import path
from . import views


urlpatterns= [
    path('products/', views.product_list),
    path('products/<int:id>/', views.product_detail),
    path('collections/', views.collection_list),
    path('collections/<int:pk>/', views.collection_detail, name='collection-detail'),
    path('orders/<int:pk>/', views.order_detail , name='order-detail'),
    path('customers/<int:pk>/', views.customer_detail , name='customer-detail'),
]