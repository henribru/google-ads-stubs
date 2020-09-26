from typing import Any, Optional

class AdGroupBidModifierServiceStub:
    GetAdGroupBidModifier: Any = ...
    MutateAdGroupBidModifiers: Any = ...
    def __init__(self, channel: Any) -> None: ...

class AdGroupBidModifierServiceServicer:
    def GetAdGroupBidModifier(self, request: Any, context: Any) -> None: ...
    def MutateAdGroupBidModifiers(self, request: Any, context: Any) -> None: ...

def add_AdGroupBidModifierServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class AdGroupBidModifierService:
    @staticmethod
    def GetAdGroupBidModifier(
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
    def MutateAdGroupBidModifiers(
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
