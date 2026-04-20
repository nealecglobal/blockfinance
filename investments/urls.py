from django.urls import path
from . import views

urlpatterns = [
    path('', views.invest_view, name='invest'),
]