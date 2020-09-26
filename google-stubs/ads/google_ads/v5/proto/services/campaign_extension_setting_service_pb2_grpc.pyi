from typing import Any, Optional

class CampaignExtensionSettingServiceStub:
    GetCampaignExtensionSetting: Any = ...
    MutateCampaignExtensionSettings: Any = ...
    def __init__(self, channel: Any) -> None: ...

class CampaignExtensionSettingServiceServicer:
    def GetCampaignExtensionSetting(self, request: Any, context: Any) -> None: ...
    def MutateCampaignExtensionSettings(self, request: Any, context: Any) -> None: ...

def add_CampaignExtensionSettingServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class CampaignExtensionSettingService:
    @staticmethod
    def GetCampaignExtensionSetting(
        request: Any,
        target: Any,
        options: Any = ...,
        channel_credentials: Optional[Any] = ...,
        call_credentials: Optional[Any] = ...,
        compression: Optional[Any] = ...,
        wait_for_ready: Optional[Any] = ...,
        timeout: Optional[Any] = ...,
        metadata: Optional[Any] = ...,
    ): ...
    @staticmethod
    def MutateCampaignExtensionSettings(
        request: Any,
        target: Any,
        options: Any = ...,
        channel_credentials: Optional[Any] = ...,
        call_credentials: Optional[Any] = ...,
        compression: Optional[Any] = ...,
        wait_for_ready: Optional[Any] = ...,
        timeout: Optional[Any] = ...,
        metadata: Optional[Any] = ...,
    ): ...
