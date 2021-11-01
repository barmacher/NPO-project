"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from account import views as account_views
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api1/v1/register/', account_views.RegisterAPIView.as_view()),
    path('api1/v1/login/', account_views.LoginAPIView.as_view()),
    path('api1/v1/confirm/', account_views.ConfirmAPIView.as_view()),
    path('api1/v1/news/', views.NewsListAPIView.as_view()),
    path('api1/v1/news/<int:pk>/', views.NewsDetailUpdateDeleteAPIView.as_view()),
    path('api1/v1/laws/<int:pk>/', views.LawsDetailUpdateDeleteAPIView.as_view()),
    path('api1/v1/publications/<int:pk>/', views.PublicationsDetailUpdateDeleteAPIView.as_view()),

    path('api1/v1/laws/', views.LawListAPIView.as_view()),
    path('api1/v1/publications/', views.PublicationListAPIView.as_view()),
    ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

