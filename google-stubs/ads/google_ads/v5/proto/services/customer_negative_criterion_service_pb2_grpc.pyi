from typing import Any, Optional

class CustomerNegativeCriterionServiceStub:
    GetCustomerNegativeCriterion: Any = ...
    MutateCustomerNegativeCriteria: Any = ...
    def __init__(self, channel: Any) -> None: ...

class CustomerNegativeCriterionServiceServicer:
    def GetCustomerNegativeCriterion(self, request: Any, context: Any) -> None: ...
    def MutateCustomerNegativeCriteria(self, request: Any, context: Any) -> None: ...

def add_CustomerNegativeCriterionServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class CustomerNegativeCriterionService:
    @staticmethod
    def GetCustomerNegativeCriterion(
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
    def MutateCustomerNegativeCriteria(
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
