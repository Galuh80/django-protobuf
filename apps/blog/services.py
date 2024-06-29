from .models import Blog
from .serializers import BlogSerializers
from django_grpc_framework import generics

class BlogService(generics.ModelService):
    
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers