from django.urls import path
from wyniki import views

urlpatterns = [
    path("", views.home, name="home"),
    path("wyniki/<name>", views.hello_there, name="hello_there"),
    path("wyniki/<name>/add", views.add_results, name="add_results"),
    path("wyniki/<name>/create_study", views.create_study, name="create_study"),
    path("wyniki/<name>/edit/<result_id>", views.edit_results, name="edit_results"),
    path("wyniki/<name>/see/<result_id>", views.see_results, name="see_results"),
    path("wyniki/<name>/history", views.history, name="history"),
    path("about/", views.about, name="about"),
]