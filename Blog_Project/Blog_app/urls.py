from django.urls import path
from Blog_app import views

app_name = 'Blog_app'

urlpatterns = [
     path('',views.PostListView.as_view(), name='post_list'),
     path('about', views.AboutView.as_view(), name='about'),
     path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
     path('post/new',views.PostCreateView.as_view(), name='post_new'),
     path('post/update/<int:pk>/', views.PostUpdateView.as_view(), name='post_edit'),
     path('post/delete/<int:pk>/', views.PostDeleteView.as_view(), name='delete'),
     path('drafts',views.PostDraftListView.as_view(), name='post_draft_list'),

     #url for the comments
     path('post/comment/<int:pk>/', views.add_comment_to_post, name='add_comment_to_post'),
     path('post/comment_approve/<int:pk>/', views.comment_approve, name='comment_approve'),
     path('post/comment_remove/<int:pk>/', views.comment_remove, name='comment_remove'),
     path('post/publish/<int:pk>/', views.post_publish, name='post_publish'),
    # Use <int:pk> for integer IDs or <slug:slug> for strings
     
]