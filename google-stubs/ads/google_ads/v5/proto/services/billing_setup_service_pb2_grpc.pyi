from typing import Any, Optional

class BillingSetupServiceStub:
    GetBillingSetup: Any = ...
    MutateBillingSetup: Any = ...
    def __init__(self, channel: Any) -> None: ...

class BillingSetupServiceServicer:
    def GetBillingSetup(self, request: Any, context: Any) -> None: ...
    def MutateBillingSetup(self, request: Any, context: Any) -> None: ...

def add_BillingSetupServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class BillingSetupService:
    @staticmethod
    def GetBillingSetup(
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
    @staticmethod
    def MutateBillingSetup(
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
