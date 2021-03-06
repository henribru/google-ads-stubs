"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.ads.google_ads.v4.proto.resources.billing_setup_pb2
import grpc

from .billing_setup_service_pb2 import *

class BillingSetupServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    def GetBillingSetup(
        self,
        request: global___GetBillingSetupRequest,
    ) -> google.ads.google_ads.v4.proto.resources.billing_setup_pb2.BillingSetup: ...
    def MutateBillingSetup(
        self,
        request: global___MutateBillingSetupRequest,
    ) -> global___MutateBillingSetupResponse: ...

class BillingSetupServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetBillingSetup(
        self,
        request: global___GetBillingSetupRequest,
        context: grpc.ServicerContext,
    ) -> google.ads.google_ads.v4.proto.resources.billing_setup_pb2.BillingSetup: ...
    @abc.abstractmethod
    def MutateBillingSetup(
        self,
        request: global___MutateBillingSetupRequest,
        context: grpc.ServicerContext,
    ) -> global___MutateBillingSetupResponse: ...

def add_BillingSetupServiceServicer_to_server(
    servicer: BillingSetupServiceServicer, server: grpc.Server
) -> None: ...
