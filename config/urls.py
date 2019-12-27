"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from blog.views import post_list, post_detail, post_add, post_delete, post_edit, post_publish, post_unpublish

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post-list/', post_list, name="post-list"),
    path('post-detail/<int:pk>/', post_detail, name="post-detail"),
    path('post-detail/<int:pk>/edit/', post_edit, name="post-edit"),
    path('post-detail/<int:pk>/publish/', post_publish, name="post-publish"),
    path('post-detail/<int:pk>/unpublish/', post_unpublish, name="post-unpublish"),
    path('post-detail/<int:pk>/delete/', post_delete, name="post-delete"),
    path('post-add/', post_add, name="post-add"),
]
