"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.ads.google_ads.v6.proto.resources.ad_group_ad_label_pb2
import grpc

from .ad_group_ad_label_service_pb2 import *

class AdGroupAdLabelServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    def GetAdGroupAdLabel(
        self,
        request: global___GetAdGroupAdLabelRequest,
    ) -> google.ads.google_ads.v6.proto.resources.ad_group_ad_label_pb2.AdGroupAdLabel: ...
    def MutateAdGroupAdLabels(
        self,
        request: global___MutateAdGroupAdLabelsRequest,
    ) -> global___MutateAdGroupAdLabelsResponse: ...

class AdGroupAdLabelServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetAdGroupAdLabel(
        self,
        request: global___GetAdGroupAdLabelRequest,
        context: grpc.ServicerContext,
    ) -> google.ads.google_ads.v6.proto.resources.ad_group_ad_label_pb2.AdGroupAdLabel: ...
    @abc.abstractmethod
    def MutateAdGroupAdLabels(
        self,
        request: global___MutateAdGroupAdLabelsRequest,
        context: grpc.ServicerContext,
    ) -> global___MutateAdGroupAdLabelsResponse: ...

def add_AdGroupAdLabelServiceServicer_to_server(
    servicer: AdGroupAdLabelServiceServicer, server: grpc.Server
) -> None: ...
