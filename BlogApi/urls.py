from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import AuthorList, BlogPostList, BlogPostDetail

urlpatterns = [
    path('authors/', AuthorList.as_view(), name='author-list'),
    path('posts/', BlogPostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', BlogPostDetail.as_view(), name='post-detail'),
    path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]

