from django.urls import path
from first_app import views

urlpatterns = [
    #path("", views.Wildflower, name='sabotage'),
    path("", views.index, name='heart'),
    path("users", views.profiles, name='loyal'),
    path("details", views.Dets, name='julie'),
    path("desc", views.Desc, name='true'),
    path("form", views.NewformMethod, name='true'),
]