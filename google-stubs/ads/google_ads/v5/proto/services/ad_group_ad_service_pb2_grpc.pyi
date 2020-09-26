from typing import Any, Optional

class AdGroupAdServiceStub:
    GetAdGroupAd: Any = ...
    MutateAdGroupAds: Any = ...
    def __init__(self, channel: Any) -> None: ...

class AdGroupAdServiceServicer:
    def GetAdGroupAd(self, request: Any, context: Any) -> None: ...
    def MutateAdGroupAds(self, request: Any, context: Any) -> None: ...

def add_AdGroupAdServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class AdGroupAdService:
    @staticmethod
    def GetAdGroupAd(
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
    def MutateAdGroupAds(
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
