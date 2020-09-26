from typing import Any, Optional

class BiddingStrategyServiceStub:
    GetBiddingStrategy: Any = ...
    MutateBiddingStrategies: Any = ...
    def __init__(self, channel: Any) -> None: ...

class BiddingStrategyServiceServicer:
    def GetBiddingStrategy(self, request: Any, context: Any) -> None: ...
    def MutateBiddingStrategies(self, request: Any, context: Any) -> None: ...

def add_BiddingStrategyServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class BiddingStrategyService:
    @staticmethod
    def GetBiddingStrategy(
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
    def MutateBiddingStrategies(
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
