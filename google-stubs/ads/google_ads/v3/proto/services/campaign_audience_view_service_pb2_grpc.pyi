from typing import Any

class CampaignAudienceViewServiceStub:
    GetCampaignAudienceView: Any = ...
    def __init__(self, channel: Any) -> None: ...

class CampaignAudienceViewServiceServicer:
    def GetCampaignAudienceView(self, request: Any, context: Any) -> None: ...

def add_CampaignAudienceViewServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...
