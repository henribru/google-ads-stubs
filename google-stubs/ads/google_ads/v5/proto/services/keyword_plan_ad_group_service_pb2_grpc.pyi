from typing import Any, Optional

class KeywordPlanAdGroupServiceStub:
    GetKeywordPlanAdGroup: Any = ...
    MutateKeywordPlanAdGroups: Any = ...
    def __init__(self, channel: Any) -> None: ...

class KeywordPlanAdGroupServiceServicer:
    def GetKeywordPlanAdGroup(self, request: Any, context: Any) -> None: ...
    def MutateKeywordPlanAdGroups(self, request: Any, context: Any) -> None: ...

def add_KeywordPlanAdGroupServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class KeywordPlanAdGroupService:
    @staticmethod
    def GetKeywordPlanAdGroup(
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
    def MutateKeywordPlanAdGroups(
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
