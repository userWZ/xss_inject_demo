from django.urls import path

from .views import Index, ReadPost, AddComment, custom_login, logout_view
urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('posts/<str:post_id>', ReadPost.as_view(), name='read-post'),
    path('add-comment', AddComment.as_view(), name='add-comment'),
    path('login/', custom_login, name='login'),
    path('logout/', logout_view, name='logout'),
]
