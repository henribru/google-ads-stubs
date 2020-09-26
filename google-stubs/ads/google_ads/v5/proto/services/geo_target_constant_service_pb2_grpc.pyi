from typing import Any, Optional

class GeoTargetConstantServiceStub:
    GetGeoTargetConstant: Any = ...
    SuggestGeoTargetConstants: Any = ...
    def __init__(self, channel: Any) -> None: ...

class GeoTargetConstantServiceServicer:
    def GetGeoTargetConstant(self, request: Any, context: Any) -> None: ...
    def SuggestGeoTargetConstants(self, request: Any, context: Any) -> None: ...

def add_GeoTargetConstantServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class GeoTargetConstantService:
    @staticmethod
    def GetGeoTargetConstant(
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
    def SuggestGeoTargetConstants(
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
