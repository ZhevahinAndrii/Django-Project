from django.urls import path

from . import views

app_name = "women_app"


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.about, name='about'),
    path('post_detail/<str:post_slug>/', views.PostView.as_view(), name='post'),
    path('posts_category/<slug:category_slug>/', views.CategoryView.as_view(), name='category'),
    path('posts_tag/<slug:tag_slug>/', views.TagView.as_view(), name='tag'),
    path('addpost/', views.AddPostView.as_view(), name='addpost'),
    path('updatepost/<str:post_slug>/', views.UpdatePostView.as_view(), name='updatepost')
]
