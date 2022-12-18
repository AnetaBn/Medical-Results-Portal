from django.urls import path
from wyniki import views

urlpatterns = [
    path("", views.home, name="home"),
    path("wyniki/<name>", views.hello_there, name="hello_there"),
    path("wyniki/<name>/add", views.add_results, name="add_results"),
    path("about/", views.about, name="about"),
]