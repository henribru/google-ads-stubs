from typing import Any, Optional

class DomainCategoryServiceStub:
    GetDomainCategory: Any = ...
    def __init__(self, channel: Any) -> None: ...

class DomainCategoryServiceServicer:
    def GetDomainCategory(self, request: Any, context: Any) -> None: ...

def add_DomainCategoryServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class DomainCategoryService:
    @staticmethod
    def GetDomainCategory(
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
