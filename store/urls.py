from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('store', views.store, name="store"),
    path('store2/', views.store2, name="store2"),
    path('store3/', views.store3, name="store3"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('showItem/', views.showItem, name="showItem"),
    path("register/", views.registerPage, name="register"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logoutUser, name="logout"),
    path('manage/', views.manage, name="manage"),
    path('custPage/', views.custPage, name="custPage"),
    path('preorder/', views.preorder, name="preorder"),


]


