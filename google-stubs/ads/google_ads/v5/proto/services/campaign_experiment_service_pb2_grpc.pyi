from typing import Any, Optional

class CampaignExperimentServiceStub:
    GetCampaignExperiment: Any = ...
    CreateCampaignExperiment: Any = ...
    MutateCampaignExperiments: Any = ...
    GraduateCampaignExperiment: Any = ...
    PromoteCampaignExperiment: Any = ...
    EndCampaignExperiment: Any = ...
    ListCampaignExperimentAsyncErrors: Any = ...
    def __init__(self, channel: Any) -> None: ...

class CampaignExperimentServiceServicer:
    def GetCampaignExperiment(self, request: Any, context: Any) -> None: ...
    def CreateCampaignExperiment(self, request: Any, context: Any) -> None: ...
    def MutateCampaignExperiments(self, request: Any, context: Any) -> None: ...
    def GraduateCampaignExperiment(self, request: Any, context: Any) -> None: ...
    def PromoteCampaignExperiment(self, request: Any, context: Any) -> None: ...
    def EndCampaignExperiment(self, request: Any, context: Any) -> None: ...
    def ListCampaignExperimentAsyncErrors(self, request: Any, context: Any) -> None: ...

def add_CampaignExperimentServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class CampaignExperimentService:
    @staticmethod
    def GetCampaignExperiment(
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
    def CreateCampaignExperiment(
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
    def MutateCampaignExperiments(
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
    def GraduateCampaignExperiment(
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
    def PromoteCampaignExperiment(
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
    def EndCampaignExperiment(
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
    def ListCampaignExperimentAsyncErrors(
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
