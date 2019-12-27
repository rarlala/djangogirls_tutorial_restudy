import os

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

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

    posts = Post.objects.all()
    context = {
        'posts' : posts
    }

    # [3번 방법]
    return render(request, 'post_list.html', context)
