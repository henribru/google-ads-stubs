from typing import Any, Optional

class CurrencyConstantServiceStub:
    GetCurrencyConstant: Any = ...
    def __init__(self, channel: Any) -> None: ...

class CurrencyConstantServiceServicer:
    def GetCurrencyConstant(self, request: Any, context: Any) -> None: ...

def add_CurrencyConstantServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class CurrencyConstantService:
    @staticmethod
    def GetCurrencyConstant(
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
