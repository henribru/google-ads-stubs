"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.ads.google_ads.v6.proto.resources.ad_group_bid_modifier_pb2
import grpc

from .ad_group_bid_modifier_service_pb2 import *

class AdGroupBidModifierServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    def GetAdGroupBidModifier(
        self,
        request: global___GetAdGroupBidModifierRequest,
    ) -> google.ads.google_ads.v6.proto.resources.ad_group_bid_modifier_pb2.AdGroupBidModifier: ...
    def MutateAdGroupBidModifiers(
        self,
        request: global___MutateAdGroupBidModifiersRequest,
    ) -> global___MutateAdGroupBidModifiersResponse: ...

class AdGroupBidModifierServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetAdGroupBidModifier(
        self,
        request: global___GetAdGroupBidModifierRequest,
        context: grpc.ServicerContext,
    ) -> google.ads.google_ads.v6.proto.resources.ad_group_bid_modifier_pb2.AdGroupBidModifier: ...
    @abc.abstractmethod
    def MutateAdGroupBidModifiers(
        self,
        request: global___MutateAdGroupBidModifiersRequest,
        context: grpc.ServicerContext,
    ) -> global___MutateAdGroupBidModifiersResponse: ...

def add_AdGroupBidModifierServiceServicer_to_server(
    servicer: AdGroupBidModifierServiceServicer, server: grpc.Server
) -> None: ...
