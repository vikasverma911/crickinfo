from django.contrib import admin
from django.urls import path, include
from .views import TeamViewSet, get_url
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'teams', TeamViewSet, basename='team')

urlpatterns = [
    path('',get_url),
]
urlpatterns = urlpatterns + router.urls
