from typing import Any

class KeywordPlanIdeaServiceStub:
    GenerateKeywordIdeas: Any = ...
    def __init__(self, channel: Any) -> None: ...

class KeywordPlanIdeaServiceServicer:
    def GenerateKeywordIdeas(self, request: Any, context: Any) -> None: ...

def add_KeywordPlanIdeaServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...
