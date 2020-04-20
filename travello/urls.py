from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('destinations/<str:name>/',views.destinations,name='destinations'),
    path('cart/<int:price>/<str:name>/',views.cart,name='cart'),
    path('review/<str:name>/',views.review,name='review'),
    path('show_cart',views.show_cart,name='show_cart'),
    path('delete_cart',views.delete_cart,name='delete_cart'),
    path('search',views.search,name='search'),
    path('about',views.about,name='about'),
    path('aboutme',views.aboutme,name='aboutme'),
    path('credits',views.credits,name='credits'),
    path('email',views.email,name='email'),
    path('checkout',views.checkout,name='checkout')
]