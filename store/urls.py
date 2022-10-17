from cgitb import lookup
from email.mime import base
from django.urls import path
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter() 
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('orders', views.OrderViewSet)
router.register('customers', views.CustomerViewSet)

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')
urlpatterns = router.urls + products_router.urls
