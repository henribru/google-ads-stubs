from typing import Any, Optional

class CampaignCriterionServiceStub:
    GetCampaignCriterion: Any = ...
    MutateCampaignCriteria: Any = ...
    def __init__(self, channel: Any) -> None: ...

class CampaignCriterionServiceServicer:
    def GetCampaignCriterion(self, request: Any, context: Any) -> None: ...
    def MutateCampaignCriteria(self, request: Any, context: Any) -> None: ...

def add_CampaignCriterionServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class CampaignCriterionService:
    @staticmethod
    def GetCampaignCriterion(
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
    def MutateCampaignCriteria(
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
