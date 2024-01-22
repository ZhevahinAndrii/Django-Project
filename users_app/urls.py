from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

app_name = 'users_app'

urlpatterns = (
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register')
)