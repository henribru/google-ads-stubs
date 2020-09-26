from typing import Any, Optional

class MobileAppCategoryConstantServiceStub:
    GetMobileAppCategoryConstant: Any = ...
    def __init__(self, channel: Any) -> None: ...

class MobileAppCategoryConstantServiceServicer:
    def GetMobileAppCategoryConstant(self, request: Any, context: Any) -> None: ...

def add_MobileAppCategoryConstantServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class MobileAppCategoryConstantService:
    @staticmethod
    def GetMobileAppCategoryConstant(
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
