from django.urls import path
from . import views

#DRF
from rest_framework.decorators import throttle_classes
from rest_framework.throttling import AnonRateThrottle
#otro estrangulador de peticiones del archivo creado throttiling
from .throttling import AnonymousUserThrottle


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path("contador/", views.numero_wsp , name="contadorultimo"),
    ]

