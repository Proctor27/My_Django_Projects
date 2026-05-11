from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # List of all posts
    path("", views.PostListView.as_view(), name='all'),
    # Create a new post
    path("new/", views.CreatePostView.as_view(), name='create'),
    # User-specific post list
    path("by/<str:username>/", views.UserPostsView.as_view(), name='for_user'),
    path("by/<str:username>/<int:pk>/", views.PostDetailView.as_view(), name='single'),
    path("delete/<int:pk>/", views.DeletePostView.as_view(), name='delete'),
]