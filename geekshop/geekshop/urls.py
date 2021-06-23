

from django.contrib import admin
from django.urls import path, include
from geekshop.views import index, contacts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('contact.html', contacts),
    path('products.html', include('mainapp.urls'))
]

