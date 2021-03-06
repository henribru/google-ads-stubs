"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.ads.google_ads.v5.proto.resources.ad_group_simulation_pb2
import grpc

from .ad_group_simulation_service_pb2 import *

class AdGroupSimulationServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    def GetAdGroupSimulation(
        self,
        request: global___GetAdGroupSimulationRequest,
    ) -> google.ads.google_ads.v5.proto.resources.ad_group_simulation_pb2.AdGroupSimulation: ...

class AdGroupSimulationServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetAdGroupSimulation(
        self,
        request: global___GetAdGroupSimulationRequest,
        context: grpc.ServicerContext,
    ) -> google.ads.google_ads.v5.proto.resources.ad_group_simulation_pb2.AdGroupSimulation: ...

def add_AdGroupSimulationServiceServicer_to_server(
    servicer: AdGroupSimulationServiceServicer, server: grpc.Server
) -> None: ...
