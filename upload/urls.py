from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),

    # Function Based View
    path('function/book/list', views.book_list, name='function-book-list'),
    path('function/book/<int:pk>', views.book_delete,
         name='function-book-delete'),
    path('function/book/upload', views.book_upload, name='function-book-upload'),

    # Class Based View
    path('class/book/list', views.book_list_view.as_view(), name='class-book-list'),
    path('class/book/upload', views.book_upload_view.as_view(),
         name='class-book-upload'),
    path('class/book/<int:pk>', views.book_delete_view.as_view(),
         name='class-book-delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
