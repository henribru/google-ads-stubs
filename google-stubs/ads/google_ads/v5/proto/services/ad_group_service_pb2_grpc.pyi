from typing import Any, Optional

class AdGroupServiceStub:
    GetAdGroup: Any = ...
    MutateAdGroups: Any = ...
    def __init__(self, channel: Any) -> None: ...

class AdGroupServiceServicer:
    def GetAdGroup(self, request: Any, context: Any) -> None: ...
    def MutateAdGroups(self, request: Any, context: Any) -> None: ...

def add_AdGroupServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class AdGroupService:
    @staticmethod
    def GetAdGroup(
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
    def MutateAdGroups(
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
