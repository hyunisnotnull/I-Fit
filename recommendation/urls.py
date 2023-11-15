from django.urls import path
from . import views

app_name = 'recommendation'

urlpatterns = [
    path("", views.recommendation, name='recommendation'),
]