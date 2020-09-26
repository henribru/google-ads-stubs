from typing import Any, Optional

class KeywordViewServiceStub:
    GetKeywordView: Any = ...
    def __init__(self, channel: Any) -> None: ...

class KeywordViewServiceServicer:
    def GetKeywordView(self, request: Any, context: Any) -> None: ...

def add_KeywordViewServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class KeywordViewService:
    @staticmethod
    def GetKeywordView(
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
