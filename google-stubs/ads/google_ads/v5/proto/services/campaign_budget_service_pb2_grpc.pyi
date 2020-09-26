from typing import Any, Optional

class CampaignBudgetServiceStub:
    GetCampaignBudget: Any = ...
    MutateCampaignBudgets: Any = ...
    def __init__(self, channel: Any) -> None: ...

class CampaignBudgetServiceServicer:
    def GetCampaignBudget(self, request: Any, context: Any) -> None: ...
    def MutateCampaignBudgets(self, request: Any, context: Any) -> None: ...

def add_CampaignBudgetServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class CampaignBudgetService:
    @staticmethod
    def GetCampaignBudget(
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
    def MutateCampaignBudgets(
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
