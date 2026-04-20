from django.urls import path
from . import views

urlpatterns = [
    path('request/', views.withdraw_request, name='withdraw_request'),
    path('pay/', views.withdraw_pay, name='withdraw_pay'),
]