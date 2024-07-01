import grpc
from google.protobuf import empty_pb2
from django_grpc_framework.services import Service
from .models import Blog
from serializers import BlogSerializer

class BlogService(Service):
    
    def List(self, request, context):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        for msg in serializer.message:
            yield msg

    def Create(self, request, context):
        serializer = BlogSerializer(message=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

    def get_object(self, pk):
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            self.context.abort(grpc.StatusCode.NOT_FOUND, 'Blog:%s not found!' % pk)

    def Retrieve(self, request, context):
        post = self.get_object(request.id)
        serializer = BlogSerializer(post)
        return serializer.message

    def Update(self, request, context):
        post = self.get_object(request.id)
        serializer = BlogSerializer(post, message=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

    def Destroy(self, request, context):
        post = self.get_object(request.id)
        post.delete()
        return empty_pb2.Empty()