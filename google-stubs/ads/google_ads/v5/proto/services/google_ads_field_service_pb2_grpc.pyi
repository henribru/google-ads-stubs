from typing import Any, Optional

class GoogleAdsFieldServiceStub:
    GetGoogleAdsField: Any = ...
    SearchGoogleAdsFields: Any = ...
    def __init__(self, channel: Any) -> None: ...

class GoogleAdsFieldServiceServicer:
    def GetGoogleAdsField(self, request: Any, context: Any) -> None: ...
    def SearchGoogleAdsFields(self, request: Any, context: Any) -> None: ...

def add_GoogleAdsFieldServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class GoogleAdsFieldService:
    @staticmethod
    def GetGoogleAdsField(
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
    def SearchGoogleAdsFields(
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
