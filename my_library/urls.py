"""my_library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from p_library import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),

    path('books/', views.books_list),
    path('authors/', views.authors_list),
    path('publishers/', views.publishers_list),
    path('friends/', views.friends_list),

    path('books_table/', views.books_table),
    path('index/book_increment/', views.book_increment),
    path('index/book_decrement/', views.book_decrement),

    path('author/create_many', views.author_create_many, name='author_create_many'),
    path('book/create_many', views.book_create_many, name='book_create_many'),
]
