from django.urls import path
from . import views
from django.shortcuts import redirect


urlpatterns = [
    path('', views.index, name='index'), 
   path('like/<int:post_id>/',views.LikeView,name='like'),
     path('delete/<int:post_id>/',views.delete,name='delete'),
    path('edit/<int:pk>/', views.edit_post, name='post_edit'),
 path('cancel/', views.cancle, name='cancel'),
]