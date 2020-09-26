from typing import Any, Optional

class CampaignLabelServiceStub:
    GetCampaignLabel: Any = ...
    MutateCampaignLabels: Any = ...
    def __init__(self, channel: Any) -> None: ...

class CampaignLabelServiceServicer:
    def GetCampaignLabel(self, request: Any, context: Any) -> None: ...
    def MutateCampaignLabels(self, request: Any, context: Any) -> None: ...

def add_CampaignLabelServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class CampaignLabelService:
    @staticmethod
    def GetCampaignLabel(
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
    def MutateCampaignLabels(
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
