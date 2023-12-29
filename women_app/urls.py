from django.urls import path

from . import views


app_name = "women_app"
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('post/<slug:post_slug>/', views.post, name='post'),
    path('category/<slug:category_slug>/', views.show_category, name='category')
]