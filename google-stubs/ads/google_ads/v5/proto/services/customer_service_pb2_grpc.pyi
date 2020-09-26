from typing import Any, Optional

class CustomerServiceStub:
    GetCustomer: Any = ...
    MutateCustomer: Any = ...
    ListAccessibleCustomers: Any = ...
    CreateCustomerClient: Any = ...
    def __init__(self, channel: Any) -> None: ...

class CustomerServiceServicer:
    def GetCustomer(self, request: Any, context: Any) -> None: ...
    def MutateCustomer(self, request: Any, context: Any) -> None: ...
    def ListAccessibleCustomers(self, request: Any, context: Any) -> None: ...
    def CreateCustomerClient(self, request: Any, context: Any) -> None: ...

def add_CustomerServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class CustomerService:
    @staticmethod
    def GetCustomer(
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
    def MutateCustomer(
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
    def ListAccessibleCustomers(
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
    def CreateCustomerClient(
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
