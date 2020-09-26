from typing import Any, Optional

class CampaignAudienceViewServiceStub:
    GetCampaignAudienceView: Any = ...
    def __init__(self, channel: Any) -> None: ...

class CampaignAudienceViewServiceServicer:
    def GetCampaignAudienceView(self, request: Any, context: Any) -> None: ...

def add_CampaignAudienceViewServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class CampaignAudienceViewService:
    @staticmethod
    def GetCampaignAudienceView(
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
