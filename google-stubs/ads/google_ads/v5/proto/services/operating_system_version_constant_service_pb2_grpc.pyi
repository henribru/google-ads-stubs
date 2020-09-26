from typing import Any, Optional

class OperatingSystemVersionConstantServiceStub:
    GetOperatingSystemVersionConstant: Any = ...
    def __init__(self, channel: Any) -> None: ...

class OperatingSystemVersionConstantServiceServicer:
    def GetOperatingSystemVersionConstant(self, request: Any, context: Any) -> None: ...

def add_OperatingSystemVersionConstantServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class OperatingSystemVersionConstantService:
    @staticmethod
    def GetOperatingSystemVersionConstant(
        request: Any,
        target: Any,
        options: Any = ...,
        channel_credentials: Optional[Any] = ...,
        call_credentials: Optional[Any] = ...,
        compression: Optional[Any] = ...,
        wait_for_ready: Optional[Any] = ...,
        timeout: Optional[Any] = ...,
        metadata: Optional[Any] = ...,
    ): ...
