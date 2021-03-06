"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.ads.google_ads.v6.proto.resources.customer_negative_criterion_pb2
import grpc

from .customer_negative_criterion_service_pb2 import *

class CustomerNegativeCriterionServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    def GetCustomerNegativeCriterion(
        self,
        request: global___GetCustomerNegativeCriterionRequest,
    ) -> google.ads.google_ads.v6.proto.resources.customer_negative_criterion_pb2.CustomerNegativeCriterion: ...
    def MutateCustomerNegativeCriteria(
        self,
        request: global___MutateCustomerNegativeCriteriaRequest,
    ) -> global___MutateCustomerNegativeCriteriaResponse: ...

class CustomerNegativeCriterionServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetCustomerNegativeCriterion(
        self,
        request: global___GetCustomerNegativeCriterionRequest,
        context: grpc.ServicerContext,
    ) -> google.ads.google_ads.v6.proto.resources.customer_negative_criterion_pb2.CustomerNegativeCriterion: ...
    @abc.abstractmethod
    def MutateCustomerNegativeCriteria(
        self,
        request: global___MutateCustomerNegativeCriteriaRequest,
        context: grpc.ServicerContext,
    ) -> global___MutateCustomerNegativeCriteriaResponse: ...

def add_CustomerNegativeCriterionServiceServicer_to_server(
    servicer: CustomerNegativeCriterionServiceServicer, server: grpc.Server
) -> None: ...
