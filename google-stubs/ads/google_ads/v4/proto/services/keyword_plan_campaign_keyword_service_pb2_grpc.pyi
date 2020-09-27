from typing import Any

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