from typing import Any

class OperatingSystemVersionConstantServiceStub:
    GetOperatingSystemVersionConstant: Any = ...
    def __init__(self, channel: Any) -> None: ...

class OperatingSystemVersionConstantServiceServicer:
    def GetOperatingSystemVersionConstant(self, request: Any, context: Any) -> None: ...

def add_OperatingSystemVersionConstantServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...
