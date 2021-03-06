"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.ads.google_ads.v5.proto.resources.account_link_pb2
import grpc

from .account_link_service_pb2 import *

class AccountLinkServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    def GetAccountLink(
        self,
        request: global___GetAccountLinkRequest,
    ) -> google.ads.google_ads.v5.proto.resources.account_link_pb2.AccountLink: ...
    def CreateAccountLink(
        self,
        request: global___CreateAccountLinkRequest,
    ) -> global___CreateAccountLinkResponse: ...
    def MutateAccountLink(
        self,
        request: global___MutateAccountLinkRequest,
    ) -> global___MutateAccountLinkResponse: ...

class AccountLinkServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetAccountLink(
        self,
        request: global___GetAccountLinkRequest,
        context: grpc.ServicerContext,
    ) -> google.ads.google_ads.v5.proto.resources.account_link_pb2.AccountLink: ...
    @abc.abstractmethod
    def CreateAccountLink(
        self,
        request: global___CreateAccountLinkRequest,
        context: grpc.ServicerContext,
    ) -> global___CreateAccountLinkResponse: ...
    @abc.abstractmethod
    def MutateAccountLink(
        self,
        request: global___MutateAccountLinkRequest,
        context: grpc.ServicerContext,
    ) -> global___MutateAccountLinkResponse: ...

def add_AccountLinkServiceServicer_to_server(
    servicer: AccountLinkServiceServicer, server: grpc.Server
) -> None: ...
