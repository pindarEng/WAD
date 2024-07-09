from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("" , views.home,name="home"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.register,name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('products/', views.productList, name='productList'),
    path('cart/add/<int:pid>/', views.addCart, name='addCart'),
    path('cart/', views.viewCart, name='viewCart'),
    path('checkout/', views.checkout, name='checkout'),
    path('add-product/', views.addProduct, name='addProduct'),

    # other URLs
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)