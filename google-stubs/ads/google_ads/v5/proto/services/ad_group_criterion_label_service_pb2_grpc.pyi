from typing import Any, Optional

class AdGroupCriterionLabelServiceStub:
    GetAdGroupCriterionLabel: Any = ...
    MutateAdGroupCriterionLabels: Any = ...
    def __init__(self, channel: Any) -> None: ...

class AdGroupCriterionLabelServiceServicer:
    def GetAdGroupCriterionLabel(self, request: Any, context: Any) -> None: ...
    def MutateAdGroupCriterionLabels(self, request: Any, context: Any) -> None: ...

def add_AdGroupCriterionLabelServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class AdGroupCriterionLabelService:
    @staticmethod
    def GetAdGroupCriterionLabel(
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
    def MutateAdGroupCriterionLabels(
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
