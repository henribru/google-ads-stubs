from typing import Any

class ConversionActionServiceStub:
    GetConversionAction: Any = ...
    MutateConversionActions: Any = ...
    def __init__(self, channel: Any) -> None: ...

class ConversionActionServiceServicer:
    def GetConversionAction(self, request: Any, context: Any) -> None: ...
    def MutateConversionActions(self, request: Any, context: Any) -> None: ...

def add_ConversionActionServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...