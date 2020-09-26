from typing import Any, Optional

class CampaignServiceStub:
    GetCampaign: Any = ...
    MutateCampaigns: Any = ...
    def __init__(self, channel: Any) -> None: ...

class CampaignServiceServicer:
    def GetCampaign(self, request: Any, context: Any) -> None: ...
    def MutateCampaigns(self, request: Any, context: Any) -> None: ...

def add_CampaignServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class CampaignService:
    @staticmethod
    def GetCampaign(
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
    def MutateCampaigns(
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
