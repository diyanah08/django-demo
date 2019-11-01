"""djangoDemo URL Configuration

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
from posts.views import index, about_us, create_post, edit_post, delete_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('profile', about_us),
    path('add', create_post),
    path('edit-post/<post_id>', edit_post),
    path('delete-post/<post_id>', delete_post)
]
