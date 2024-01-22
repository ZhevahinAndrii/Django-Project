from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Ім`я користувача", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label="Ім`я користувача")
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Підтвердіть пароль', widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'password2')
        labels = {
            'email': 'Адреса електронної пошти',
            'first_name': "Ім'я",
            'last_name': 'Прізвище'
        }

    def clean_password2(self):
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            raise forms.ValidationError('Паролі не збігаються')
        return self.cleaned_data['password2']

    def clean_email(self):
        if get_user_model().objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError('Користувач з такою адресою електронної пошти вже існує')
        return self.cleaned_data['email']