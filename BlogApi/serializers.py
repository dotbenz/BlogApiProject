from rest_framework import serializers
from .models import Author, BlogPost

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'user', 'bio']

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'author', 'timestamp']
