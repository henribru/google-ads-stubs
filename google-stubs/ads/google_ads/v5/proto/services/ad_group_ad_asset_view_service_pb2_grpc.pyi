from typing import Any, Optional

class AdGroupAdAssetViewServiceStub:
    GetAdGroupAdAssetView: Any = ...
    def __init__(self, channel: Any) -> None: ...

class AdGroupAdAssetViewServiceServicer:
    def GetAdGroupAdAssetView(self, request: Any, context: Any) -> None: ...

def add_AdGroupAdAssetViewServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class AdGroupAdAssetViewService:
    @staticmethod
    def GetAdGroupAdAssetView(
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
