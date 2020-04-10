from typing import Any

class CampaignLabelServiceStub:
    GetCampaignLabel: Any = ...
    MutateCampaignLabels: Any = ...
    def __init__(self, channel: Any) -> None: ...

class CampaignLabelServiceServicer:
    def GetCampaignLabel(self, request: Any, context: Any) -> None: ...
    def MutateCampaignLabels(self, request: Any, context: Any) -> None: ...

def add_CampaignLabelServiceServicer_to_server(servicer: Any, server: Any) -> None: ...
