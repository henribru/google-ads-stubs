from typing import Any, Optional

class AssetServiceStub:
    GetAsset: Any = ...
    MutateAssets: Any = ...
    def __init__(self, channel: Any) -> None: ...

class AssetServiceServicer:
    def GetAsset(self, request: Any, context: Any) -> None: ...
    def MutateAssets(self, request: Any, context: Any) -> None: ...

def add_AssetServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class AssetService:
    @staticmethod
    def GetAsset(
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
    def MutateAssets(
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
