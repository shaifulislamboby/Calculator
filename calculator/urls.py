from django.urls import path
from . import views

urlpatterns = [
    path('calculator/', views.Calculate.as_view(), name='calculator-endpoint'),
]
