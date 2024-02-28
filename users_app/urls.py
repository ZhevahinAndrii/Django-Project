from django.contrib.auth.views import LogoutView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, reverse_lazy

from . import views
from .forms import UserPasswordResetForm

app_name = 'users_app'

urlpatterns = (
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('profile/', views.ProfileUserView.as_view(), name='profile'),
    path('password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name='users_app/password_change_done.html'),
         name='password_change_done'),
    path('password-reset/', PasswordResetView.as_view(template_name='users_app/password_reset_form.html',
                                                      form_class=UserPasswordResetForm,
                                                      email_template_name='users_app/password_reset_email.html',
                                                      success_url=reverse_lazy('users_app:password_reset_done')
                                                      ), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users_app/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users_app/password_reset_confirm.html',
                                                                              success_url=reverse_lazy('users_app:password_reset_complete')),
                                                                                name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(template_name='users_app/password_reset_complete.html'),
                                                                                name='password_reset_complete')

)
