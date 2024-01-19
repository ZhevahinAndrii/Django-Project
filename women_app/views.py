import uuid

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, FormView, CreateView

import women_app.services as services
from .forms import AddPostForm, UploadFileForm
from .models import Woman, UploadFilesModel

menu = [{'title': 'About site', 'url_name': "women:about"}, {'title': 'Add page', 'url_name': 'women:addpage'}]
categories = [
    {'id': 1, 'name': 'Actresses'},
    {'id': 2, 'name': 'Singers'}
]


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


def show_post(request: WSGIRequest, post_slug: str):
    post_to_show: Woman = services.get_single_published_post_with_tags_or_404(slug=post_slug)
    data = {
        'title': post_to_show.title,
        'menu': menu,
        'post': post_to_show,
        'category_selected': post_to_show.category_id
    }
    return render(request, 'women/post.html', context=data)


class PostView(DetailView):
    template_name = 'women/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_object(self, queryset=None):
        return services.get_single_published_post_with_tags_or_404(slug=self.kwargs[self.slug_url_kwarg])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context[self.context_object_name].title
        context['menu'] = menu
        context['category_selected'] = context[self.context_object_name].category_id
        return context


def show_category(request: WSGIRequest, category_slug: str):
    category = services.get_post_category_or_404(slug=category_slug)
    posts = category.posts.filter(status=Woman.Status.PUBLISHED).defer('status', 'husband_id', 'time_created')
    context = {
        'title': f'Категорія: {category.name}',
        'menu': menu,
        'category_selected': category.pk,
        'posts': posts
    }
    return render(request, 'women/index.html', context=context)


def show_tag(request: WSGIRequest, tag_slug: str):
    tag = services.get_post_tag_or_404(slug=tag_slug)
    posts = tag.posts.filter(status=Woman.Status.PUBLISHED).select_related('category').defer('status', 'time_created',
                                                                                             'husband_id',
                                                                                             'category__slug')
    context = {
        'title': f'Тег: {tag.title}',
        'menu': menu,
        'posts': posts,
        'category_selected': None
    }
    return render(request, 'women/index.html', context=context)


class IndexView(ListView):
    template_name = 'women/index.html'
    queryset = services.get_all_published_posts().select_related("category").defer('status', 'category__slug',
                                                                                   'time_created',
                                                                                   'husband_id')
    context_object_name = 'posts'
    extra_context = {
        'title': 'Домашня сторінка',
        'menu': menu,
        'category_selected': 0
    }


class CategoryView(ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return (Woman.published.filter(category__slug=self.kwargs['category_slug']).select_related('category').
                defer('status', 'time_created', 'husband_id', 'category__slug'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = services.get_post_category_or_404(slug=self.kwargs['category_slug'])
        context['title'] = f'Категорія: {category.name}'
        context['menu'] = menu
        context['category_selected'] = category.pk
        return context


class TagView(ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return (Woman.published.filter(tags__slug=self.kwargs['tag_slug']).select_related('category').
                defer('status', 'time_created', 'husband_id', 'category__slug'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = services.get_post_tag_or_404(slug=self.kwargs['tag_slug'])
        context['title'] = f'Тег: {tag.title}'
        context['menu'] = menu
        context['category_selected'] = None
        return context


class AddPageView(View):
    @staticmethod
    def get(request):
        return render(request, 'women/addpage.html',
                      {'menu': menu, 'title': 'Додавання публікації', 'form': AddPostForm()})

    @staticmethod
    def post(request):
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('women:index')
        return render(request, 'women/addpage.html', {'menu': menu, 'title': 'Додавання публікації', 'form': form})


# class AddPostView(FormView):
#     template_name = 'women/addpage.html'
#     form_class = AddPostForm
#     success_url = reverse_lazy('women:index')
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


class AddPostView(CreateView):
    template_name = 'women/addpage.html'
    form_class = AddPostForm
    # success_url = reverse_lazy('women:index') if you don`t use success url it will be automatically redirected
    # to get_absolute_url of created object

