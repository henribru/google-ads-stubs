from typing import Any

class AdScheduleViewServiceStub:
    GetAdScheduleView: Any = ...
    def __init__(self, channel: Any) -> None: ...

class AdScheduleViewServiceServicer:
    def GetAdScheduleView(self, request: Any, context: Any) -> None: ...

def add_AdScheduleViewServiceServicer_to_server(servicer: Any, server: Any) -> None: ...
