from typing import Any, Optional

class BatchJobServiceStub:
    MutateBatchJob: Any = ...
    GetBatchJob: Any = ...
    ListBatchJobResults: Any = ...
    RunBatchJob: Any = ...
    AddBatchJobOperations: Any = ...
    def __init__(self, channel: Any) -> None: ...

class BatchJobServiceServicer:
    def MutateBatchJob(self, request: Any, context: Any) -> None: ...
    def GetBatchJob(self, request: Any, context: Any) -> None: ...
    def ListBatchJobResults(self, request: Any, context: Any) -> None: ...
    def RunBatchJob(self, request: Any, context: Any) -> None: ...
    def AddBatchJobOperations(self, request: Any, context: Any) -> None: ...

def add_BatchJobServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class BatchJobService:
    @staticmethod
    def MutateBatchJob(
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
    def GetBatchJob(
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
    def ListBatchJobResults(
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
    def RunBatchJob(
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
    def AddBatchJobOperations(
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
