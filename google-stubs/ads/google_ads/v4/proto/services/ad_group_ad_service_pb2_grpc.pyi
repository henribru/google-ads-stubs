"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.ads.google_ads.v4.proto.resources.ad_group_ad_pb2
import grpc

from .ad_group_ad_service_pb2 import *

class AdGroupAdServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    def GetAdGroupAd(
        self,
        request: global___GetAdGroupAdRequest,
    ) -> google.ads.google_ads.v4.proto.resources.ad_group_ad_pb2.AdGroupAd: ...
    def MutateAdGroupAds(
        self,
        request: global___MutateAdGroupAdsRequest,
    ) -> global___MutateAdGroupAdsResponse: ...

class AdGroupAdServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetAdGroupAd(
        self,
        request: global___GetAdGroupAdRequest,
        context: grpc.ServicerContext,
    ) -> google.ads.google_ads.v4.proto.resources.ad_group_ad_pb2.AdGroupAd: ...
    @abc.abstractmethod
    def MutateAdGroupAds(
        self,
        request: global___MutateAdGroupAdsRequest,
        context: grpc.ServicerContext,
    ) -> global___MutateAdGroupAdsResponse: ...

def add_AdGroupAdServiceServicer_to_server(
    servicer: AdGroupAdServiceServicer, server: grpc.Server
) -> None: ...
