"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.ads.google_ads.v5.proto.resources.campaign_extension_setting_pb2
import grpc

from .campaign_extension_setting_service_pb2 import *

class CampaignExtensionSettingServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    def GetCampaignExtensionSetting(
        self,
        request: global___GetCampaignExtensionSettingRequest,
    ) -> google.ads.google_ads.v5.proto.resources.campaign_extension_setting_pb2.CampaignExtensionSetting: ...
    def MutateCampaignExtensionSettings(
        self,
        request: global___MutateCampaignExtensionSettingsRequest,
    ) -> global___MutateCampaignExtensionSettingsResponse: ...

class CampaignExtensionSettingServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetCampaignExtensionSetting(
        self,
        request: global___GetCampaignExtensionSettingRequest,
        context: grpc.ServicerContext,
    ) -> google.ads.google_ads.v5.proto.resources.campaign_extension_setting_pb2.CampaignExtensionSetting: ...
    @abc.abstractmethod
    def MutateCampaignExtensionSettings(
        self,
        request: global___MutateCampaignExtensionSettingsRequest,
        context: grpc.ServicerContext,
    ) -> global___MutateCampaignExtensionSettingsResponse: ...

def add_CampaignExtensionSettingServiceServicer_to_server(
    servicer: CampaignExtensionSettingServiceServicer, server: grpc.Server
) -> None: ...
