from typing import Any, Optional

class CampaignDraftServiceStub:
    GetCampaignDraft: Any = ...
    MutateCampaignDrafts: Any = ...
    PromoteCampaignDraft: Any = ...
    ListCampaignDraftAsyncErrors: Any = ...
    def __init__(self, channel: Any) -> None: ...

class CampaignDraftServiceServicer:
    def GetCampaignDraft(self, request: Any, context: Any) -> None: ...
    def MutateCampaignDrafts(self, request: Any, context: Any) -> None: ...
    def PromoteCampaignDraft(self, request: Any, context: Any) -> None: ...
    def ListCampaignDraftAsyncErrors(self, request: Any, context: Any) -> None: ...

def add_CampaignDraftServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class CampaignDraftService:
    @staticmethod
    def GetCampaignDraft(
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
    def MutateCampaignDrafts(
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
    def PromoteCampaignDraft(
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
    def ListCampaignDraftAsyncErrors(
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
