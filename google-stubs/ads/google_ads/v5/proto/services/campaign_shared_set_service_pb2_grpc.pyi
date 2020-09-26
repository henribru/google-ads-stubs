from typing import Any, Optional

class CampaignSharedSetServiceStub:
    GetCampaignSharedSet: Any = ...
    MutateCampaignSharedSets: Any = ...
    def __init__(self, channel: Any) -> None: ...

class CampaignSharedSetServiceServicer:
    def GetCampaignSharedSet(self, request: Any, context: Any) -> None: ...
    def MutateCampaignSharedSets(self, request: Any, context: Any) -> None: ...

def add_CampaignSharedSetServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class CampaignSharedSetService:
    @staticmethod
    def GetCampaignSharedSet(
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
    def MutateCampaignSharedSets(
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
