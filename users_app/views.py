from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from .forms import LoginUserForm, RegisterUserForm, ProfileUserForm, UserPasswordChangeForm


# def LoginUserView(request: WSGIRequest):
#     if request.method == 'POST':
#         form = LoginUserForm(request.POST)
#         if form.is_valid():
#             cleaned_data = form.cleaned_data
#             user: AbstractBaseUser = authenticate(request, username=cleaned_data['username'], password=cleaned_data['password'])
#             if user and user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('women_app:index'))
#     form = LoginUserForm()
#     return render(request, 'users_app/login.html', {'form': form})


def user_not_logged_in(user):
    return not user.is_authenticated


@method_decorator(user_passes_test(user_not_logged_in, login_url=reverse_lazy('women_app:index')), name='dispatch')
class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'users_app/login.html'
    extra_context = {'title': 'Авторизація'}


def register(request: WSGIRequest):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'users_app/register_done.html')
    else:
        form = RegisterUserForm()
    return render(request, 'users_app/register.html', {'form': form})


class RegisterUserView(CreateView):
    template_name = 'users_app/register.html'
    form_class = RegisterUserForm
    extra_context = {'title': 'Реєстрація'}
    success_url = reverse_lazy('users_app:login')


class ProfileUserView(LoginRequiredMixin, UpdateView):
    authentication_classes = []
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users_app/profile.html'
    extra_context = {'title': 'Профіль користувача'}

    def get_success_url(self):
        return reverse_lazy('users_app:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordChangeView(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy('users_app:password_change_done')
    template_name = 'users_app/password_change_form.html'


