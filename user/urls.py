from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path("user/", views.user, name='user'),
    path("compare", views.compare, name='compare'),

    # 다른 URL 패턴들
]