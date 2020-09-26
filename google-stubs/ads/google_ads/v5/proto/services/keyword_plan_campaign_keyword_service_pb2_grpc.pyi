from typing import Any, Optional

class KeywordPlanCampaignKeywordServiceStub:
    GetKeywordPlanCampaignKeyword: Any = ...
    MutateKeywordPlanCampaignKeywords: Any = ...
    def __init__(self, channel: Any) -> None: ...

class KeywordPlanCampaignKeywordServiceServicer:
    def GetKeywordPlanCampaignKeyword(self, request: Any, context: Any) -> None: ...
    def MutateKeywordPlanCampaignKeywords(self, request: Any, context: Any) -> None: ...

def add_KeywordPlanCampaignKeywordServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class KeywordPlanCampaignKeywordService:
    @staticmethod
    def GetKeywordPlanCampaignKeyword(
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
    def MutateKeywordPlanCampaignKeywords(
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
