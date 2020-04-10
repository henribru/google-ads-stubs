from typing import Any

class SharedCriterionServiceStub:
    GetSharedCriterion: Any = ...
    MutateSharedCriteria: Any = ...
    def __init__(self, channel: Any) -> None: ...

class SharedCriterionServiceServicer:
    def GetSharedCriterion(self, request: Any, context: Any) -> None: ...
    def MutateSharedCriteria(self, request: Any, context: Any) -> None: ...

def add_SharedCriterionServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...
