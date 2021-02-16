"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webs.urls')),
    path('kontak', include('webs.urls')),
    path('katalog', include('webs.urls')),
    path('pembayaran', include('webs.urls')),
    path('showrooms', include('webs.urls')),
    path('product1', include('webs.urls')),
    path('product2', include('webs.urls')),
    path('product3', include('webs.urls')),
    path('product4', include('webs.urls')),
    path('product5', include('webs.urls')),
    path('product6', include('webs.urls')),
    path('product7', include('webs.urls')),
    path('product8', include('webs.urls')),
    path('product9', include('webs.urls')),
    path('product10', include('webs.urls')),
    path('product11', include('webs.urls')),
    path('about', include('webs.urls')),

]
