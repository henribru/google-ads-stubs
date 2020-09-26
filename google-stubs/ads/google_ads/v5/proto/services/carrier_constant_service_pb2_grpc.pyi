from typing import Any, Optional

class CarrierConstantServiceStub:
    GetCarrierConstant: Any = ...
    def __init__(self, channel: Any) -> None: ...

class CarrierConstantServiceServicer:
    def GetCarrierConstant(self, request: Any, context: Any) -> None: ...

def add_CarrierConstantServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class CarrierConstantService:
    @staticmethod
    def GetCarrierConstant(
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
