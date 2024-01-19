import copy
import uuid

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

import women_app.services as services
from .forms import AddPostForm, UploadFileForm
from .models import Woman, UploadFilesModel
from .utils import DataMixin

menu = [{'title': 'Про сайт', 'url_name': "women:about"},
        {'title': 'Додавання публікації', 'url_name': 'women:addpost'}]


def handle_uploaded_file(f):
    with open(f'uploads/{f.name}---{uuid.uuid4()}', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def about(request: WSGIRequest):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_model = UploadFilesModel(file=form.cleaned_data['file'])
            file_model.save()
    else:
        form = UploadFileForm()
    context = {
        'title': 'Про сайт',
        'menu': menu,
        'form': form

    }
    return render(request, 'women/about.html', context=context)


class IndexView(DataMixin, ListView):
    template_name = 'women/index.html'
    queryset = services.get_all_published_posts().select_related("category").defer('status', 'category__slug',
                                                                                   'time_created',
                                                                                   'husband_id')
    context_object_name = 'posts'
    title = 'Домашня сторінка'
    category_selected = 0


class CategoryView(DataMixin, ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return (Woman.published.filter(category__slug=self.kwargs['category_slug']).select_related('category').
                defer('status', 'time_created', 'husband_id', 'category__slug'))

    def get_context_data(self, **kwargs):
        category = services.get_post_category_or_404(slug=self.kwargs['category_slug'])
        context = super().get_context_data(**kwargs)
        context = self.get_mixin_context(context, title=f'Категорія: {category.name}', category_selected=category.pk)
        return context


class TagView(DataMixin, ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return (Woman.published.filter(tags__slug=self.kwargs['tag_slug']).select_related('category').
                defer('status', 'time_created', 'husband_id', 'category__slug'))

    def get_context_data(self, **kwargs):
        tag = services.get_post_tag_or_404(slug=self.kwargs['tag_slug'])
        context = super().get_context_data(**kwargs)
        context = self.get_mixin_context(context, title=f'Тег: {tag.title}')
        return context


# class AddPostView(FormView):
#     template_name = 'women/addpost.html'
#     form_class = AddPostForm
#     success_url = reverse_lazy('women:index')
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
class PostView(DataMixin, DetailView):
    template_name = 'women/post_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_object(self, queryset=None):
        return services.get_single_published_post_with_tags_or_404(slug=self.kwargs[self.slug_url_kwarg])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = self.get_mixin_context(context, title=context[self.context_object_name].title,
                                         category_selected=context[self.context_object_name].category_id)
        post_menu = copy.copy(menu)
        post_menu.append({'title': 'Оновлення публікації', 'url_name': 'women:updatepost'})
        context['menu'] = post_menu
        return context


class AddPostView(DataMixin, CreateView):
    template_name = 'women/addpost.html'
    form_class = AddPostForm
    success_url = reverse_lazy('women:index')
    # if you don`t use success url it will be automatically redirected
    # to get_absolute_url of created object#
    title = 'Додавання публікації'


class UpdatePostView(UpdateView):
    template_name = 'women/addpost.html'
    form_class = AddPostForm
    success_url = reverse_lazy('women:index')

    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    title = 'Оновлення публікації'

    def get_object(self, queryset=None):
        return get_object_or_404(
            Woman.objects.prefetch_related('tags').defer('time_created', 'time_last_modified', 'slug'),
            slug=self.kwargs[self.slug_url_kwarg])
