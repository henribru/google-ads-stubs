from typing import Any

class AdGroupAudienceViewServiceStub:
    GetAdGroupAudienceView: Any = ...
    def __init__(self, channel: Any) -> None: ...

class AdGroupAudienceViewServiceServicer:
    def GetAdGroupAudienceView(self, request: Any, context: Any) -> None: ...

def add_AdGroupAudienceViewServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...
