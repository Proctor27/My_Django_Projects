from django.urls import path
from Third_app import views

urlpatterns = [
    path("", views.index, name='sabotage'),
    path("forms", views.battle, name='sabotage'),
]