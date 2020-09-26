from typing import Any, Optional

class GoogleAdsServiceStub:
    Search: Any = ...
    SearchStream: Any = ...
    Mutate: Any = ...
    def __init__(self, channel: Any) -> None: ...

class GoogleAdsServiceServicer:
    def Search(self, request: Any, context: Any) -> None: ...
    def SearchStream(self, request: Any, context: Any) -> None: ...
    def Mutate(self, request: Any, context: Any) -> None: ...

def add_GoogleAdsServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class GoogleAdsService:
    @staticmethod
    def Search(
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
    def SearchStream(
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
    def Mutate(
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
