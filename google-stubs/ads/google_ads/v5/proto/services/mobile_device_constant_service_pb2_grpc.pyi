from typing import Any, Optional

class MobileDeviceConstantServiceStub:
    GetMobileDeviceConstant: Any = ...
    def __init__(self, channel: Any) -> None: ...

class MobileDeviceConstantServiceServicer:
    def GetMobileDeviceConstant(self, request: Any, context: Any) -> None: ...

def add_MobileDeviceConstantServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class MobileDeviceConstantService:
    @staticmethod
    def GetMobileDeviceConstant(
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
