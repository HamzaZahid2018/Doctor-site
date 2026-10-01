from django.urls import path
from django.views.generic import RedirectView
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', RedirectView.as_view(pattern_name='website:home', permanent=True), name='contact_redirect'),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),
]
