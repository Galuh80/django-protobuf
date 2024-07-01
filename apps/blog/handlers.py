from services import BlogService
from proto import blog_pb2_grpc


def grpc_handlers(server):
    blog_pb2_grpc.add_BlogControllerServicer_to_server(BlogService.as_servicer(), server)