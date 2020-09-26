from typing import Any, Optional

class IncomeRangeViewServiceStub:
    GetIncomeRangeView: Any = ...
    def __init__(self, channel: Any) -> None: ...

class IncomeRangeViewServiceServicer:
    def GetIncomeRangeView(self, request: Any, context: Any) -> None: ...

def add_IncomeRangeViewServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class IncomeRangeViewService:
    @staticmethod
    def GetIncomeRangeView(
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
