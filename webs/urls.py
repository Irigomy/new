
from django.urls import path
from . import views

urlpatterns = [
            path('', views.post_list, name='post_list'),
            path('kontak', views.kontak, name='kontak'),
            path('katalog', views.katalog, name='katalog'),
            path('pembayaran', views.pembayaran, name='pembayaran'),
            path('showrooms', views.showrooms, name='showrooms'),
            path('product1', views.product1, name='product1'),
   	    path('product2', views.product2, name='product2'),
    	    path('product3', views.product3, name='product3'),
    	    path('product4', views.product4, name='product4'),
   	    path('product5', views.product5, name='product5'),
    	    path('product6', views.product6, name='product6'),
            path('product7', views.product7, name='product7'),
    	    path('product8', views.product8, name='product8'),
    	    path('product9', views.product9, name='product9'),
    	    path('product10', views.product10, name='product10'),
   	    path('product11', views.product11, name='product11'),
            path('about', views.about, name='about'),
]
