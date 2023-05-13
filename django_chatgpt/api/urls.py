from django.urls import path

from django_chatgpt.api import views

urlpatterns = [
    path("ask/", views.ask, name="ask"),
]
