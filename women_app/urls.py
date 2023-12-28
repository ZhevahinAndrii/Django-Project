from django.urls import path

from . import views


app_name = "women_app"
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('post/<int:post_id>/', views.post, name='post'),
    path('category/<int:category_id>/', views.show_category, name='category')
]