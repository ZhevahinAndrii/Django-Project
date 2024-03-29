from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, PasswordResetForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Ім`я користувача", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Ім`я користувача", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Підтвердіть пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        labels = {
            'email': 'Адреса електронної пошти',
            'first_name': "Ім'я",
            'last_name': 'Прізвище'
        }
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'})
        }

    # def clean_password2(self):
    #     if self.cleaned_data['password'] != self.cleaned_data['password2']:
    #         raise forms.ValidationError('Паролі не збігаються')
    #     return self.cleaned_data['password2']

    def clean_email(self):
        if get_user_model().objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError('Користувач з такою адресою електронної пошти вже існує')
        return self.cleaned_data['email']


class ProfileUserForm(forms.ModelForm):
    email = forms.CharField(disabled=True, label='Адреса електронної пошти', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name')
        labels = {
            'email': 'Адреса електронної пошти',
            'username': "Ім'я користувача",
            'first_name': "Ім'я",
            'last_name': 'Прізвище'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'})
        }


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Старий пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password1 = forms.CharField(label='Новий пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password2 = forms.CharField(label='Підтвердження паролю', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='Адреса електронної пошти', max_length=254, widget=forms.EmailInput(attrs={"autocomplete": "email"}))


