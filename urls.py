from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='list'),
    path('post/<int:pk>/', views.detail, name='detail'),
    path('post/create/', views.create, name='create'),
    path('post/<int:pk>/manage/', views.manage, name='manage'),
    path('post/<int:pk>/comment/add/', views.add_comment, name='add_comment'),
    path('comment/<int:pk>/edit/', views.edit_comment, name='edit_comment'),
]