from django.urls import path, include
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    TestApi
)
from . import views

from blog.views import PostViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView
)

router=DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),#cannot name template as post_create.html because CreateView automatically uses the pattern:<app_name>/<model_name>_form.html
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),#Django handles the form logic but we still need a template such as:blog/post_form.html
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),#requireds post_confirm_delete.html
    #DRF
    path('api-auth/',include('rest_framework.urls')),
    path('test/',TestApi.as_view(),name='test-view'),
    path('test/<int:pk>/',TestApi.as_view(),name='test-viewdetail'),
    path('api/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    
]
urlpatterns += router.urls
#passwordistoocommon
