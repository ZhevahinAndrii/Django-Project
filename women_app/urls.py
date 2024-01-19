from django.urls import path

from . import views


app_name = "women_app"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.about, name='about'),
    path('post/<str:post_slug>/', views.PostView.as_view(), name='post'),
    path('category/<slug:category_slug>/', views.CategoryView.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', views.TagView.as_view(), name='tag'),
    path('addpage/', views.AddPostView.as_view(), name='addpage')
]