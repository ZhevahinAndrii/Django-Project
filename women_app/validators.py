from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class UkrainianValidator:
    ALLOWED_CHARS = 'ЙЦУКЕНГШЩЗХЇФІВАПРОЛДЖЄЯЧСМИТЬБЮйцукенгшщзхїфівапролджєячсмитьбю0123456789- '
    code = 'ukrainian'

    def __init__(self, message=None):
        self.message = message if message else 'В заголовку мають бути лише українські літери, цифри, дефіс або пробіл'

    def __call__(self, value, *args, **kwargs):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise ValidationError(self.message, code=self.code)
