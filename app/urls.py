from django.contrib import admin
from django.urls import path, include
from .views import FindTeamView

urlpatterns = [
    path('',FindTeamView.as_view()),
]
