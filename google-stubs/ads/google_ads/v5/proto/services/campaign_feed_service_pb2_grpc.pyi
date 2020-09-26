from typing import Any, Optional

class CampaignFeedServiceStub:
    GetCampaignFeed: Any = ...
    MutateCampaignFeeds: Any = ...
    def __init__(self, channel: Any) -> None: ...

class CampaignFeedServiceServicer:
    def GetCampaignFeed(self, request: Any, context: Any) -> None: ...
    def MutateCampaignFeeds(self, request: Any, context: Any) -> None: ...

def add_CampaignFeedServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class CampaignFeedService:
    @staticmethod
    def GetCampaignFeed(
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
    def MutateCampaignFeeds(
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
