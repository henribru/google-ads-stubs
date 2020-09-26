from typing import Any, Optional

class ProductGroupViewServiceStub:
    GetProductGroupView: Any = ...
    def __init__(self, channel: Any) -> None: ...

class ProductGroupViewServiceServicer:
    def GetProductGroupView(self, request: Any, context: Any) -> None: ...

def add_ProductGroupViewServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class ProductGroupViewService:
    @staticmethod
    def GetProductGroupView(
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
