"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.ads.google_ads.v4.proto.resources.ad_schedule_view_pb2
import grpc

from .ad_schedule_view_service_pb2 import *

class AdScheduleViewServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    def GetAdScheduleView(
        self,
        request: global___GetAdScheduleViewRequest,
    ) -> google.ads.google_ads.v4.proto.resources.ad_schedule_view_pb2.AdScheduleView: ...

class AdScheduleViewServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetAdScheduleView(
        self,
        request: global___GetAdScheduleViewRequest,
        context: grpc.ServicerContext,
    ) -> google.ads.google_ads.v4.proto.resources.ad_schedule_view_pb2.AdScheduleView: ...

def add_AdScheduleViewServiceServicer_to_server(
    servicer: AdScheduleViewServiceServicer, server: grpc.Server
) -> None: ...
