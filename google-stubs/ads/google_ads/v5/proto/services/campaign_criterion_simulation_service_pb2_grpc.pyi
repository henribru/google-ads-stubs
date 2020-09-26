from typing import Any, Optional

class CampaignCriterionSimulationServiceStub:
    GetCampaignCriterionSimulation: Any = ...
    def __init__(self, channel: Any) -> None: ...

class CampaignCriterionSimulationServiceServicer:
    def GetCampaignCriterionSimulation(self, request: Any, context: Any) -> None: ...

def add_CampaignCriterionSimulationServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class CampaignCriterionSimulationService:
    @staticmethod
    def GetCampaignCriterionSimulation(
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
