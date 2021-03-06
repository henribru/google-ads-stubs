"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.ads.google_ads.v6.proto.resources.customer_manager_link_pb2
import grpc

from .customer_manager_link_service_pb2 import *

class CustomerManagerLinkServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    def GetCustomerManagerLink(
        self,
        request: global___GetCustomerManagerLinkRequest,
    ) -> google.ads.google_ads.v6.proto.resources.customer_manager_link_pb2.CustomerManagerLink: ...
    def MutateCustomerManagerLink(
        self,
        request: global___MutateCustomerManagerLinkRequest,
    ) -> global___MutateCustomerManagerLinkResponse: ...
    def MoveManagerLink(
        self,
        request: global___MoveManagerLinkRequest,
    ) -> global___MoveManagerLinkResponse: ...

class CustomerManagerLinkServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetCustomerManagerLink(
        self,
        request: global___GetCustomerManagerLinkRequest,
        context: grpc.ServicerContext,
    ) -> google.ads.google_ads.v6.proto.resources.customer_manager_link_pb2.CustomerManagerLink: ...
    @abc.abstractmethod
    def MutateCustomerManagerLink(
        self,
        request: global___MutateCustomerManagerLinkRequest,
        context: grpc.ServicerContext,
    ) -> global___MutateCustomerManagerLinkResponse: ...
    @abc.abstractmethod
    def MoveManagerLink(
        self,
        request: global___MoveManagerLinkRequest,
        context: grpc.ServicerContext,
    ) -> global___MoveManagerLinkResponse: ...

def add_CustomerManagerLinkServiceServicer_to_server(
    servicer: CustomerManagerLinkServiceServicer, server: grpc.Server
) -> None: ...
