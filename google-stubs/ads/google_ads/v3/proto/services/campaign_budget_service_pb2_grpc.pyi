from typing import Any

class CampaignBudgetServiceStub:
    GetCampaignBudget: Any = ...
    MutateCampaignBudgets: Any = ...
    def __init__(self, channel: Any) -> None: ...

class CampaignBudgetServiceServicer:
    def GetCampaignBudget(self, request: Any, context: Any) -> None: ...
    def MutateCampaignBudgets(self, request: Any, context: Any) -> None: ...

def add_CampaignBudgetServiceServicer_to_server(servicer: Any, server: Any) -> None: ...
