from django.urls import path
from Three_Seconds_Passwords import views

#Template Tagging or URLS
app_name = 'Three_Seconds_Passwords'
urlpatterns = [
    path('register',views.register,name='register'),
    path('user_login',views.user_login,name='user_login'),
] 