from typing import Any

class DisplayKeywordViewServiceStub:
    GetDisplayKeywordView: Any = ...
    def __init__(self, channel: Any) -> None: ...

class DisplayKeywordViewServiceServicer:
    def GetDisplayKeywordView(self, request: Any, context: Any) -> None: ...

def add_DisplayKeywordViewServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...
