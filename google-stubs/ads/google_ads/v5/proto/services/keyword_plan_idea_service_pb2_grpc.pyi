from typing import Any, Optional

class KeywordPlanIdeaServiceStub:
    GenerateKeywordIdeas: Any = ...
    def __init__(self, channel: Any) -> None: ...

class KeywordPlanIdeaServiceServicer:
    def GenerateKeywordIdeas(self, request: Any, context: Any) -> None: ...

def add_KeywordPlanIdeaServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class KeywordPlanIdeaService:
    @staticmethod
    def GenerateKeywordIdeas(
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
