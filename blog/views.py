import os

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.utils import timezone

from blog.models import Post


def post_list(request):
    # [1번 방법]
    # current_file_path = os.path.abspath(__file__)
    # blog_file_path = os.path.dirname(current_file_path)
    # root_file_path = os.path.dirname(blog_file_path)
    #
    # templates_file_path = os.path.join(root_file_path, 'templates')
    # post_list_html_path = os.path.join(templates_file_path, 'post_list.html')
    #
    # f = open(post_list_html_path, 'rt')
    # html = f.read()
    # f.close()
    #
    # return HttpResponse(html)

    # [2번 방법]
    # content = loader.render_to_string('post_list.html', None, request)
    # return HttpResponse(content)

    # posts = Post.objects.all()
    posts = Post.objects.order_by('-pk')

    context = {
        'posts': posts
    }

    # [3번 방법]
    return render(request, 'post_list.html', context)


def post_detail(request, pk):
    # [1번 방법]
    # try:
    #     posts = Post.objects.filter(pk=pk)
    #     post = posts[0]
    # except:
    #     return HttpResponse('없음')
    #
    # context = {
    #     'post': post,
    # }
    #
    # return render(request, 'post_detail.html', context)

    # [2번 방법]
    post = get_object_or_404(Post, pk=pk)

    context = {
        'post': post
    }

    return render(request, 'post_detail.html', context)


def post_add(request):
    if request.method == 'POST':
        author = request.user
        title = request.POST['title']
        text = request.POST['text']

        post = Post.objects.create(
            title=title,
            author=author,
            text=text,
        )
        return redirect('post-list')

    else:
        return render(request, 'post_add.html')


def post_delete(request, pk):
    if request.method == 'POST':
        Post.objects.filter(pk=pk).delete()
        return redirect('post-list')
    else:
        post = get_object_or_404(Post, pk=pk)
        context = {
            'post': post
        }
        return render(request, 'post_delete.html', context)


def post_edit(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']

        post.title = title
        post.text = text
        post.save()
        return redirect('post-detail', pk=pk)

    else:
        context = {
            'post': post
        }
        return render(request, 'post_edit.html', context)


def post_publish(request, pk):
    post = Post.objects.get(pk=pk)
    post.published_date = timezone.now()
    post.save()
    return redirect('post-detail', pk=pk)


def post_unpublish(request, pk):
    post = Post.objects.get(pk=pk)
    post.published_date = None
    post.save()
    return redirect('post-detail', pk=pk)
