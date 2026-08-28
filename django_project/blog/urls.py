from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/str:<username>/', UserPostListView.as_view(), name='user-posts'),
    path('about/', views.about, name='blog-about'),
    path('post/int:<pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),#cannot name template as post_create.html because CreateView automatically uses the pattern:<app_name>/<model_name>_form.html
    path('post/int:<pk>/update/',PostUpdateView.as_view(),name='post-update'),#Django handles the form logic but we still need a template such as:blog/post_form.html
    path('post/int:<pk>/delete/',PostDeleteView.as_view(),name='post-delete'),#requireds post_confirm_delete.html
]
#passwordistoocommon
