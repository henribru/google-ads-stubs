"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.ads.google_ads.v4.proto.resources.ad_group_criterion_pb2
import grpc

from .ad_group_criterion_service_pb2 import *

class AdGroupCriterionServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    def GetAdGroupCriterion(
        self,
        request: global___GetAdGroupCriterionRequest,
    ) -> google.ads.google_ads.v4.proto.resources.ad_group_criterion_pb2.AdGroupCriterion: ...
    def MutateAdGroupCriteria(
        self,
        request: global___MutateAdGroupCriteriaRequest,
    ) -> global___MutateAdGroupCriteriaResponse: ...

class AdGroupCriterionServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetAdGroupCriterion(
        self,
        request: global___GetAdGroupCriterionRequest,
        context: grpc.ServicerContext,
    ) -> google.ads.google_ads.v4.proto.resources.ad_group_criterion_pb2.AdGroupCriterion: ...
    @abc.abstractmethod
    def MutateAdGroupCriteria(
        self,
        request: global___MutateAdGroupCriteriaRequest,
        context: grpc.ServicerContext,
    ) -> global___MutateAdGroupCriteriaResponse: ...

def add_AdGroupCriterionServiceServicer_to_server(
    servicer: AdGroupCriterionServiceServicer, server: grpc.Server
) -> None: ...
