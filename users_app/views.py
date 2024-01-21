from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from .forms import LoginUserForm

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


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'users_app/login.html'
    extra_context = {'title': 'Авторизація'}

    # def get_success_url(self):
    #     return reverse('women_app:index')
