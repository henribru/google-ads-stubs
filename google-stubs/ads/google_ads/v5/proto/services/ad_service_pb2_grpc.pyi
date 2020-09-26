from typing import Any, Optional

class AdServiceStub:
    GetAd: Any = ...
    MutateAds: Any = ...
    def __init__(self, channel: Any) -> None: ...

class AdServiceServicer:
    def GetAd(self, request: Any, context: Any) -> None: ...
    def MutateAds(self, request: Any, context: Any) -> None: ...

def add_AdServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class AdService:
    @staticmethod
    def GetAd(
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
    def MutateAds(
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
