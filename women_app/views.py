import uuid


from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

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


def addpage(request):
    if request.method == "POST":
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('women:index')
    else:
        form = AddPostForm()
    return render(request, 'women/addpage.html', {'menu': menu, 'title': 'Додавання публікації', 'form': form})


class IndexView(TemplateView):
    template_name = 'women/index.html'
    extra_context = {
        'title': 'Домашня сторінка',
        'menu': menu,
        'posts': services.get_all_published_posts().select_related("category").defer('status', 'category__slug',
                                                                                     'time_created',
                                                                                     'husband_id'),
        'category_selected': 0
    }


class AddPageView(View):
    def get(self, request):
        return render(request, 'women/addpage.html', {'menu': menu, 'title': 'Додавання публікації', 'form': AddPostForm()})

    def post(self, request):
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('women:index')
        return render(request, 'women/addpage.html', {'menu': menu, 'title': 'Додавання публікації', 'form': form})