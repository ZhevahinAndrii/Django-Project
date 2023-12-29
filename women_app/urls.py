from django.urls import path

from . import views


app_name = "women_app"
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('post/<slug:post_slug>/', views.show_post, name='post'),
    path('category/<slug:category_slug>/', views.show_category, name='category'),
    path('tag/<slug:tag_slug>/', views.show_tag, name='tag')
]