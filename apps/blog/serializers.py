from .models import Blog
from django_grpc_framework import proto_serializers
from proto import blog_pb2

class BlogSerializers(proto_serializers.ModelProtoSerializer):
    
    class Meta:
        model = Blog
        proto_class = blog_pb2.Blog
        fields = ['id','title','content']