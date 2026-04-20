from django.urls import path
from Barbie import views

urlpatterns = [
    path("", views.lady, name='heart'),
] 