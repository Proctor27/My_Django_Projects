from django.urls import path
from ClassBasedViews import views

app_name = 'ClassBasedViews'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
    # Use <int:pk> for integer IDs or <slug:slug> for strings
    path('<int:pk>/', views.SchoolDetailView.as_view(), name='detail'),
    path('create',views.SchoolCreateView.as_view(), name='create'),
     path('Update/<int:pk>/', views.SchoolUpdateView.as_view(), name='update'),
     path('delete/<int:pk>/', views.SchoolDeleteView.as_view(), name='delete'),
]