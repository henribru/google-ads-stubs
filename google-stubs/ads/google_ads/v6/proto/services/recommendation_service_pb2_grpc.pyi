# Stubs for google.ads.google_ads.v6.proto.services.recommendation_service_pb2_grpc (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class RecommendationServiceStub:
    GetRecommendation: Any = ...
    ApplyRecommendation: Any = ...
    DismissRecommendation: Any = ...
    def __init__(self, channel: Any) -> None: ...

class RecommendationServiceServicer:
    def GetRecommendation(self, request: Any, context: Any) -> None: ...
    def ApplyRecommendation(self, request: Any, context: Any) -> None: ...
    def DismissRecommendation(self, request: Any, context: Any) -> None: ...

def add_RecommendationServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class RecommendationService:
    @staticmethod
    def GetRecommendation(
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
    def ApplyRecommendation(
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
    def DismissRecommendation(
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