menu = [{'title': 'Про сайт', 'url_name': "women_app:about"},
        {'title': 'Додавання публікації', 'url_name': 'women_app:addpost'}]


class DataMixin:
    title = None
    category_selected = None
    extra_context = {}
    paginate_by = 3

    def __init__(self):
        if self.title:
            self.extra_context['title'] = self.title
        self.extra_context['category_selected'] = self.category_selected

    def get_mixin_context(self, context, **kwargs):
        context.update(**self.extra_context)
        context.update(kwargs)
        return context
