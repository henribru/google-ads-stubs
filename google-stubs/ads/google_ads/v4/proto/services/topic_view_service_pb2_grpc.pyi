"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.ads.google_ads.v4.proto.resources.topic_view_pb2
import grpc

from .topic_view_service_pb2 import *

class TopicViewServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    def GetTopicView(
        self,
        request: global___GetTopicViewRequest,
    ) -> google.ads.google_ads.v4.proto.resources.topic_view_pb2.TopicView: ...

class TopicViewServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetTopicView(
        self,
        request: global___GetTopicViewRequest,
        context: grpc.ServicerContext,
    ) -> google.ads.google_ads.v4.proto.resources.topic_view_pb2.TopicView: ...

def add_TopicViewServiceServicer_to_server(
    servicer: TopicViewServiceServicer, server: grpc.Server
) -> None: ...
