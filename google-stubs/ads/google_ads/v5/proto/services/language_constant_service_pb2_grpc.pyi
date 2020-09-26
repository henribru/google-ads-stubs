from typing import Any, Optional

class LanguageConstantServiceStub:
    GetLanguageConstant: Any = ...
    def __init__(self, channel: Any) -> None: ...

class LanguageConstantServiceServicer:
    def GetLanguageConstant(self, request: Any, context: Any) -> None: ...

def add_LanguageConstantServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class LanguageConstantService:
    @staticmethod
    def GetLanguageConstant(
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
