from typing import Any, Optional

class CampaignAssetServiceStub:
    GetCampaignAsset: Any = ...
    MutateCampaignAssets: Any = ...
    def __init__(self, channel: Any) -> None: ...

class CampaignAssetServiceServicer:
    def GetCampaignAsset(self, request: Any, context: Any) -> None: ...
    def MutateCampaignAssets(self, request: Any, context: Any) -> None: ...

def add_CampaignAssetServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class CampaignAssetService:
    @staticmethod
    def GetCampaignAsset(
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
    def MutateCampaignAssets(
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
