from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("hakkimizda", views.about, name="about"),
    path("iletisim", views.contact, name="contact")
]
