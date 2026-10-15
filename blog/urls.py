from django.urls import path
from . import views


urlpatterns = [

    # Home
    path("", views.home, name="home"),

    # Introduction pages
    path("about/", views.about, name="about"),
    path("study/", views.study, name="study"),
    path("skills/", views.skills, name="skills"),
    path("projects/", views.projects, name="projects"),
    path("dream/", views.dream, name="dream"),
    path("contact/", views.contact, name="contact"),

    # User Registration
    path("register/", views.RegisterView.as_view(), name="register"),

    # CRUD
    path("posts/", views.post_list, name="post_list"),
    path("posts/create/", views.post_create, name="post_create"),
    path("posts/<int:pk>/", views.post_detail, name="post_detail"),
    path("posts/<int:pk>/edit/", views.post_edit, name="post_edit"),
    path("posts/<int:pk>/delete/", views.post_delete, name="post_delete"),

]