from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('products/', views.product_list, name='product_list'),
    path('products/addProduct/',views.addProduct,name='addProduct'),
    path('products/<int:product_id>/delete/', views.delete_product, name='delete_product'),
    path('products/<int:product_id>/modify/', views.modify_product, name='modify_product'),
    # Other URLs
]
