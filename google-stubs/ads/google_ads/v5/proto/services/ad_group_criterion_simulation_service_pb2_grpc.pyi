from typing import Any, Optional

class AdGroupCriterionSimulationServiceStub:
    GetAdGroupCriterionSimulation: Any = ...
    def __init__(self, channel: Any) -> None: ...

class AdGroupCriterionSimulationServiceServicer:
    def GetAdGroupCriterionSimulation(self, request: Any, context: Any) -> None: ...

def add_AdGroupCriterionSimulationServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class AdGroupCriterionSimulationService:
    @staticmethod
    def GetAdGroupCriterionSimulation(
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
