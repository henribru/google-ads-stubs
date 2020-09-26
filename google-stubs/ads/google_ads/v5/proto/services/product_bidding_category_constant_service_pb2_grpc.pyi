from typing import Any, Optional

class ProductBiddingCategoryConstantServiceStub:
    GetProductBiddingCategoryConstant: Any = ...
    def __init__(self, channel: Any) -> None: ...

class ProductBiddingCategoryConstantServiceServicer:
    def GetProductBiddingCategoryConstant(self, request: Any, context: Any) -> None: ...

def add_ProductBiddingCategoryConstantServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class ProductBiddingCategoryConstantService:
    @staticmethod
    def GetProductBiddingCategoryConstant(
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
