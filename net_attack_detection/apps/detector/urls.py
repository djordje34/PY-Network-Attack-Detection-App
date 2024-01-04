from django.contrib import admin
from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import show_form, predict, diagnose,get_data

urlpatterns = [
    path('predict/', predict, name='predict'),
    path('diagnose/', diagnose, name='diagnose'),
    path('show_form/', show_form, name='show_form'),
    path('', views.index, name="index"),
    path('get_data/',get_data,name='get_data'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
