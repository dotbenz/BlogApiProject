from rest_framework import generics
from .models import Author, BlogPost
from .serializers import AuthorSerializer, BlogPostSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BlogPostList(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination

class BlogPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated]

