from typing import Any

class AdParameterServiceStub:
    GetAdParameter: Any = ...
    MutateAdParameters: Any = ...
    def __init__(self, channel: Any) -> None: ...

class AdParameterServiceServicer:
    def GetAdParameter(self, request: Any, context: Any) -> None: ...
    def MutateAdParameters(self, request: Any, context: Any) -> None: ...

def add_AdParameterServiceServicer_to_server(servicer: Any, server: Any) -> None: ...