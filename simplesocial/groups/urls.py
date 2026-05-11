from django.urls import path
from groups import views

app_name = 'groups'

urlpatterns = [
    path("",views.ListGroupView.as_view(),name='all'),
    path("new/",views.CreateGroupView.as_view(),name='create'),
    path("posts/in/<slug:slug>/",views.SingleGroupView.as_view(),name='single'),
    path("join/<slug:slug>/",views.JoinGroupView.as_view(),name='join'),
    path("leave/<slug:slug>/",views.LeaveGroupView.as_view(),name='leave'),
]