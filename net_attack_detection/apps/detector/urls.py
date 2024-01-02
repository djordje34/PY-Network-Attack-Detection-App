from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from .views import show_form, process_form, predict, diagnose

urlpatterns = [
    path('predict/', predict, name='predict'),
    path('diagnose/', diagnose, name='diagnose'),
    path('show_form/', show_form, name='show_form'),
    path('process_form/', process_form, name='process_form'),
    re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
