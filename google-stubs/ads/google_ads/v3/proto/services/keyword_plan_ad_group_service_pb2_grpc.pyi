from typing import Any

class KeywordPlanAdGroupServiceStub:
    GetKeywordPlanAdGroup: Any = ...
    MutateKeywordPlanAdGroups: Any = ...
    def __init__(self, channel: Any) -> None: ...

class KeywordPlanAdGroupServiceServicer:
    def GetKeywordPlanAdGroup(self, request: Any, context: Any) -> None: ...
    def MutateKeywordPlanAdGroups(self, request: Any, context: Any) -> None: ...

def add_KeywordPlanAdGroupServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...