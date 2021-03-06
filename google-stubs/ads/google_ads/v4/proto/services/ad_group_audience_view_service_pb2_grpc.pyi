"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.ads.google_ads.v4.proto.resources.ad_group_audience_view_pb2
import grpc

from .ad_group_audience_view_service_pb2 import *

class AdGroupAudienceViewServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    def GetAdGroupAudienceView(
        self,
        request: global___GetAdGroupAudienceViewRequest,
    ) -> google.ads.google_ads.v4.proto.resources.ad_group_audience_view_pb2.AdGroupAudienceView: ...

class AdGroupAudienceViewServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetAdGroupAudienceView(
        self,
        request: global___GetAdGroupAudienceViewRequest,
        context: grpc.ServicerContext,
    ) -> google.ads.google_ads.v4.proto.resources.ad_group_audience_view_pb2.AdGroupAudienceView: ...

def add_AdGroupAudienceViewServiceServicer_to_server(
    servicer: AdGroupAudienceViewServiceServicer, server: grpc.Server
) -> None: ...
