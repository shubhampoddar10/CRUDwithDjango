from django.contrib import admin
from django.conf.urls import url,include

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'booksapp/',include('booksapp.urls')),
    url(r'cities/',include('cities.urls')),

]
