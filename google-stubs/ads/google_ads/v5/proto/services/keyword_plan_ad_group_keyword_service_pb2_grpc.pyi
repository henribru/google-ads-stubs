from typing import Any, Optional

class KeywordPlanAdGroupKeywordServiceStub:
    GetKeywordPlanAdGroupKeyword: Any = ...
    MutateKeywordPlanAdGroupKeywords: Any = ...
    def __init__(self, channel: Any) -> None: ...

class KeywordPlanAdGroupKeywordServiceServicer:
    def GetKeywordPlanAdGroupKeyword(self, request: Any, context: Any) -> None: ...
    def MutateKeywordPlanAdGroupKeywords(self, request: Any, context: Any) -> None: ...

def add_KeywordPlanAdGroupKeywordServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class KeywordPlanAdGroupKeywordService:
    @staticmethod
    def GetKeywordPlanAdGroupKeyword(
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
    def MutateKeywordPlanAdGroupKeywords(
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
