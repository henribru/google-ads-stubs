"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.ads.google_ads.v6.proto.resources.feed_placeholder_view_pb2
import grpc

from .feed_placeholder_view_service_pb2 import *

class FeedPlaceholderViewServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    def GetFeedPlaceholderView(
        self,
        request: global___GetFeedPlaceholderViewRequest,
    ) -> google.ads.google_ads.v6.proto.resources.feed_placeholder_view_pb2.FeedPlaceholderView: ...

class FeedPlaceholderViewServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetFeedPlaceholderView(
        self,
        request: global___GetFeedPlaceholderViewRequest,
        context: grpc.ServicerContext,
    ) -> google.ads.google_ads.v6.proto.resources.feed_placeholder_view_pb2.FeedPlaceholderView: ...

def add_FeedPlaceholderViewServiceServicer_to_server(
    servicer: FeedPlaceholderViewServiceServicer, server: grpc.Server
) -> None: ...
