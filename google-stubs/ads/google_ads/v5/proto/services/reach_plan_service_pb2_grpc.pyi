from typing import Any, Optional

class ReachPlanServiceStub:
    ListPlannableLocations: Any = ...
    ListPlannableProducts: Any = ...
    GenerateProductMixIdeas: Any = ...
    GenerateReachForecast: Any = ...
    def __init__(self, channel: Any) -> None: ...

class ReachPlanServiceServicer:
    def ListPlannableLocations(self, request: Any, context: Any) -> None: ...
    def ListPlannableProducts(self, request: Any, context: Any) -> None: ...
    def GenerateProductMixIdeas(self, request: Any, context: Any) -> None: ...
    def GenerateReachForecast(self, request: Any, context: Any) -> None: ...

def add_ReachPlanServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class ReachPlanService:
    @staticmethod
    def ListPlannableLocations(
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
    def ListPlannableProducts(
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
    def GenerateProductMixIdeas(
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
    def GenerateReachForecast(
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
