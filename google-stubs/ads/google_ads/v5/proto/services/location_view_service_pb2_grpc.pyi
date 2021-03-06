"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.ads.google_ads.v5.proto.resources.location_view_pb2
import grpc

from .location_view_service_pb2 import *

class LocationViewServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    def GetLocationView(
        self,
        request: global___GetLocationViewRequest,
    ) -> google.ads.google_ads.v5.proto.resources.location_view_pb2.LocationView: ...

class LocationViewServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetLocationView(
        self,
        request: global___GetLocationViewRequest,
        context: grpc.ServicerContext,
    ) -> google.ads.google_ads.v5.proto.resources.location_view_pb2.LocationView: ...

def add_LocationViewServiceServicer_to_server(
    servicer: LocationViewServiceServicer, server: grpc.Server
) -> None: ...
