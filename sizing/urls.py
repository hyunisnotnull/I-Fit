"""
URL configuration for sizing project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),  # 기본 관리자 URL은 그대로 유지
    path("", include("main.urls")),  # /main/ 경로를 main 앱의 URL과 연결
    path("accounts/", include("accounts.urls")), # accounts 경로
    path("user/", include("user.urls")),  # /user/ 경로를 user 앱의 URL과 연결
    path("clothes/", include("clothes.urls")),  # /clothes/ 경로를 clothes 앱의 URL과 연결
    path("recommendation/", include("recommendation.urls")),  # /recommendation/ 경로를 recommendation 앱의 URL과 연결
    path("reviews/", include("reviews.urls")),
]
