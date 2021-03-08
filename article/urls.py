from django.urls import path
from article import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('all_post/', views.SeePostView.as_view(), name='see_post'),
]
