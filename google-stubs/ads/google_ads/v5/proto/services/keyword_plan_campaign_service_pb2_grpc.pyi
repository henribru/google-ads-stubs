from typing import Any, Optional

class KeywordPlanCampaignServiceStub:
    GetKeywordPlanCampaign: Any = ...
    MutateKeywordPlanCampaigns: Any = ...
    def __init__(self, channel: Any) -> None: ...

class KeywordPlanCampaignServiceServicer:
    def GetKeywordPlanCampaign(self, request: Any, context: Any) -> None: ...
    def MutateKeywordPlanCampaigns(self, request: Any, context: Any) -> None: ...

def add_KeywordPlanCampaignServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class KeywordPlanCampaignService:
    @staticmethod
    def GetKeywordPlanCampaign(
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
    def MutateKeywordPlanCampaigns(
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
