from django.urls import path
from django.urls.resolvers import URLPattern
from . import views







urlpatterns = [
    path('', views.home,name='home'),
    path('products/', views.products,name='products'),
    # path('customer/', views.customer,name='customer'),


    #Now we are going to make the path dynamic
    #it will target a customer by 
    # example 'customer/1'
    # for that we have to use <> barckets


    path('customer/<str:pk_test>/',views.customer, name='customer'),

    path('create_order/<str:pk>/',views.createOrder, name='create_order'),
    path('update_order/<str:pk>/', views.updateOrder, name = 'update_order'),
    path('delete_order/<str:pk>/', views.deleteOrder, name= 'delete_order'),
    path('login/', views.loginPage, name= 'login'),
    path('register/', views.registerPage, name= 'register'),
    path('logout/', views.logoutUser, name= 'logout'),

]