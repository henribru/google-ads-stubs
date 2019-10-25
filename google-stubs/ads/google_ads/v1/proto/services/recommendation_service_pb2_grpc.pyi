# Stubs for google.ads.google_ads.v1.proto.services.recommendation_service_pb2_grpc (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

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