from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("addUser/",views.addUser,name="addUser"),
    path("viewUsers/",views.viewUsers,name="viewUsers"),
    path("addProdcut/",views.addProduct,name="addProduct"),
    path("viewProducts/",views.viewProducts,name="viewProducts"),
    path("findProducts/",views.findProducts,name="findProducts"),
]