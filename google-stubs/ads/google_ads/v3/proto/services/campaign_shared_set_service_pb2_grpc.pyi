from typing import Any

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
