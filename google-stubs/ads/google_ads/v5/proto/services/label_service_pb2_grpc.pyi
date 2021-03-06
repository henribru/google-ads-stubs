"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.ads.google_ads.v5.proto.resources.label_pb2
import grpc

from .label_service_pb2 import *

class LabelServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    def GetLabel(
        self,
        request: global___GetLabelRequest,
    ) -> google.ads.google_ads.v5.proto.resources.label_pb2.Label: ...
    def MutateLabels(
        self,
        request: global___MutateLabelsRequest,
    ) -> global___MutateLabelsResponse: ...

class LabelServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetLabel(
        self,
        request: global___GetLabelRequest,
        context: grpc.ServicerContext,
    ) -> google.ads.google_ads.v5.proto.resources.label_pb2.Label: ...
    @abc.abstractmethod
    def MutateLabels(
        self,
        request: global___MutateLabelsRequest,
        context: grpc.ServicerContext,
    ) -> global___MutateLabelsResponse: ...

def add_LabelServiceServicer_to_server(
    servicer: LabelServiceServicer, server: grpc.Server
) -> None: ...
