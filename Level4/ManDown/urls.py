from django.urls import path
from ManDown import views

#Template Tagging
app_name = 'ManDown'
urlpatterns = [
    path('',views.index,name='index'),
    path('base',views.base,name='base'),
    path('other',views.otherpage,name='otherpage'),
    path('relative',views.relative,name='relative'),
]