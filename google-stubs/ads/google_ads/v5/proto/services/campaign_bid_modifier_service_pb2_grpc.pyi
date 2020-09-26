from typing import Any, Optional

class CampaignBidModifierServiceStub:
    GetCampaignBidModifier: Any = ...
    MutateCampaignBidModifiers: Any = ...
    def __init__(self, channel: Any) -> None: ...

class CampaignBidModifierServiceServicer:
    def GetCampaignBidModifier(self, request: Any, context: Any) -> None: ...
    def MutateCampaignBidModifiers(self, request: Any, context: Any) -> None: ...

def add_CampaignBidModifierServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class CampaignBidModifierService:
    @staticmethod
    def GetCampaignBidModifier(
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
    def MutateCampaignBidModifiers(
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
