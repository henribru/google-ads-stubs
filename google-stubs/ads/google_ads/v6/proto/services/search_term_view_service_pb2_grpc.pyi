"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.ads.google_ads.v6.proto.resources.search_term_view_pb2
import grpc

from .search_term_view_service_pb2 import *

class SearchTermViewServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    def GetSearchTermView(
        self,
        request: global___GetSearchTermViewRequest,
    ) -> google.ads.google_ads.v6.proto.resources.search_term_view_pb2.SearchTermView: ...

class SearchTermViewServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetSearchTermView(
        self,
        request: global___GetSearchTermViewRequest,
        context: grpc.ServicerContext,
    ) -> google.ads.google_ads.v6.proto.resources.search_term_view_pb2.SearchTermView: ...

def add_SearchTermViewServiceServicer_to_server(
    servicer: SearchTermViewServiceServicer, server: grpc.Server
) -> None: ...
