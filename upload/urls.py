from . import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),

    # Function Based View
    path('function/book/list', views.book_list, name='function-book-list'),
    path('function/book/<int:pk>', views.book_delete,
         name='function-book-delete'),
    path('function/book/upload', views.book_upload, name='function-book-upload'),

    # Class Based View
    path('class/book/list', views.book_list_view.as_view(), name='class-book-list'),
    path('class/book/upload', views.book_upload_view.as_view(),
         name='class-book-upload'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
