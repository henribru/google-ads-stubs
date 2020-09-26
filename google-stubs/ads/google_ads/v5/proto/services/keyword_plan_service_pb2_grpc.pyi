from typing import Any, Optional

class KeywordPlanServiceStub:
    GetKeywordPlan: Any = ...
    MutateKeywordPlans: Any = ...
    GenerateForecastCurve: Any = ...
    GenerateForecastTimeSeries: Any = ...
    GenerateForecastMetrics: Any = ...
    GenerateHistoricalMetrics: Any = ...
    def __init__(self, channel: Any) -> None: ...

class KeywordPlanServiceServicer:
    def GetKeywordPlan(self, request: Any, context: Any) -> None: ...
    def MutateKeywordPlans(self, request: Any, context: Any) -> None: ...
    def GenerateForecastCurve(self, request: Any, context: Any) -> None: ...
    def GenerateForecastTimeSeries(self, request: Any, context: Any) -> None: ...
    def GenerateForecastMetrics(self, request: Any, context: Any) -> None: ...
    def GenerateHistoricalMetrics(self, request: Any, context: Any) -> None: ...

def add_KeywordPlanServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class KeywordPlanService:
    @staticmethod
    def GetKeywordPlan(
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
    def MutateKeywordPlans(
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
    def GenerateForecastCurve(
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
    def GenerateForecastTimeSeries(
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
    def GenerateForecastMetrics(
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
    def GenerateHistoricalMetrics(
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
