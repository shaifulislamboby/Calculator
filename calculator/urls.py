from django.urls import path, re_path
from . import views

urlpatterns = [
    path('calculator/', views.Calculate.as_view(), name='calculator-endpoint'),
    # re_path(r'^calculator/(?:expression=(?P<expression>\w+))$', views.Calculate.as_view(), name='calculator-endpoint'),
    # good
]
