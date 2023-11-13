from django.urls import path
from . import views

app_name = 'recommendation'

urlpatterns = [
    path("recommendation/", views.recommendation, name='recommendation'),
]