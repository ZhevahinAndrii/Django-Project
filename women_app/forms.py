from django import forms
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

from .models import WomanCategory, Man, Woman


@deconstructible
class UkrainianValidator:
    ALLOWED_CHARS = 'ЙЦУКЕНГШЩЗХЇФІВАПРОЛДЖЄЯЧСМИТЬБЮйцукенгшщзхїфівапролджєячсмитьбю0123456789- '
    code = 'ukrainian'

    def __init__(self, message=None):
        self.message = message if message else 'В заголовку мають бути лише українські літери, цифри, дефіс або пробіл'

    def __call__(self, value, *args, **kwargs):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise ValidationError(self.message, code=self.code)


class AddPostForm(forms.ModelForm):
    # title = forms.CharField(label='Заголовок',
    #                         validators=[MinLengthValidator(5, message='Заголовок має містити хоча б 5 символів'),
    #                                     MaxLengthValidator(100, message='Заголовок має містити максимум 100 символів')],
    #                         widget=forms.TextInput(attrs={'class': 'form-input'}),
    #                         error_messages={'required': 'Публікація має містити заголовок'})
    # # slug = forms.SlugField(max_length=255, label='URL', allow_unicode=True)
    # content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}), required=False, label='Зміст',
    #                           empty_value='Content')
    # status = forms.ChoiceField(choices=((0, 'Чернетка'), (1, 'Опубліковано')), label='Статус', initial=1)
    category = forms.ModelChoiceField(queryset=WomanCategory.objects.all(), label='Категорія', empty_label='Не обрано', required=False)
    husband = forms.ModelChoiceField(queryset=Man.objects.filter(wife__isnull=True), required=False, label='Чоловік',
                                     empty_label='Незаміжня')

    class Meta:
        model = Woman

        fields = ('title', 'content', 'photo', 'status', 'category', 'husband', 'tags')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'напр.: Анджеліна Джолі'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        allowed_chars = 'ЙЦУКЕНГШЩЗХЇФІВАПРОЛДЖЄЯЧСМИТЬБЮйцукенгшщзхїфівапролджєячсмитьбю0123456789- '
        if not set(title) <= set(allowed_chars):
            raise ValidationError('В заголовку мають бути лише українські літери, цифри, дефіс або пробіл',
                                  code='ukrainian')
        return title


class UploadFileForm(forms.Form):
    file = forms.ImageField(label='Файл')