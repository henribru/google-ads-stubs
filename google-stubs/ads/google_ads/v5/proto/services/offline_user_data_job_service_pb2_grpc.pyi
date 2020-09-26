from typing import Any, Optional

class OfflineUserDataJobServiceStub:
    CreateOfflineUserDataJob: Any = ...
    GetOfflineUserDataJob: Any = ...
    AddOfflineUserDataJobOperations: Any = ...
    RunOfflineUserDataJob: Any = ...
    def __init__(self, channel: Any) -> None: ...

class OfflineUserDataJobServiceServicer:
    def CreateOfflineUserDataJob(self, request: Any, context: Any) -> None: ...
    def GetOfflineUserDataJob(self, request: Any, context: Any) -> None: ...
    def AddOfflineUserDataJobOperations(self, request: Any, context: Any) -> None: ...
    def RunOfflineUserDataJob(self, request: Any, context: Any) -> None: ...

def add_OfflineUserDataJobServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class OfflineUserDataJobService:
    @staticmethod
    def CreateOfflineUserDataJob(
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
    def GetOfflineUserDataJob(
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
    def AddOfflineUserDataJobOperations(
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
    def RunOfflineUserDataJob(
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
