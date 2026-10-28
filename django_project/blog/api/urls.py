from django.urls import path, include
# from .views import TestApi
from .views import PostViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView
)

router=DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    #DRF
    path('api-auth/',include('rest_framework.urls')),
    # path('api/<str:version>/test/',TestApi.as_view(),name='test-view'),
    # path('test/',TestApi.as_view(),name='test-view'),
    # path('test/<int:pk>/',TestApi.as_view(),name='test-viewdetail'),
    path('api/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
   
]
urlpatterns += router.urls