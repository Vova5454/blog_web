from django.urls import path
from . import views


app_name = "about"

urlpatterns = [
    path("", views.about_author, name="about"),
    path("tech/", views.tech, name="tech")
]
