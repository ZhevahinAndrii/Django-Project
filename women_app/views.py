import copy

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

import women_app.services as services
from .forms import AddPostForm
from .models import Woman
from .utils import DataMixin, menu


def about(request: WSGIRequest):
    posts = services.get_all_published_posts()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        'title': 'Про сайт',
        'menu': menu,
        'page': page
    }
    return render(request, 'women_app/about.html', context=context)


class IndexView(DataMixin, ListView):
    template_name = 'women_app/index.html'
    queryset = services.get_all_published_posts().select_related("category", 'author').only('slug', 'title', 'content',
                                                                                            'time_last_modified',
                                                                                            'photo',
                                                                                            'category__name',
                                                                                            'author__username')
    # queryset = services.get_all_published_posts().select_related("category").defer('status', 'category__slug',
    #                                                                                'time_created',
    #                                                                                'husband_id').select_related('author').defer('')
    context_object_name = 'posts'
    title = 'Домашня сторінка'
    category_selected = 0


class CategoryView(DataMixin, ListView):
    template_name = 'women_app/index.html'
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
    template_name = 'women_app/index.html'
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
#     template_name = 'women_app/addpost.html'
#     form_class = AddPostForm
#     success_url = reverse_lazy('women_app:index')
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
class PostView(DataMixin, DetailView):
    template_name = 'women_app/post_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_object(self, queryset=None):
        return services.get_single_published_post_with_tags_or_404(slug=self.kwargs[self.slug_url_kwarg])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = self.get_mixin_context(context, title=context[self.context_object_name].title,
                                         category_selected=context[self.context_object_name].category_id)
        return context


class AddPostView(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, CreateView):
    template_name = 'women_app/addpost.html'
    form_class = AddPostForm
    success_url = reverse_lazy('women_app:index')
    permission_required = 'women_app.add_woman'
    # if you don`t use success url it will be automatically redirected
    # to get_absolute_url of created object#
    title = 'Додавання публікації'

    def form_valid(self, form):
        woman: Woman = form.save(commit=False)
        woman.author = self.request.user
        return super().form_valid(form)


class UpdatePostView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    template_name = 'women_app/addpost.html'
    form_class = AddPostForm
    success_url = reverse_lazy('women_app:index')
    permission_required = 'women_app.change_woman'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    title = 'Оновлення публікації'

    def get_object(self, queryset=None):
        return get_object_or_404(
            Woman.objects.prefetch_related('tags').defer('time_created', 'time_last_modified'),
            slug=self.kwargs[self.slug_url_kwarg])
