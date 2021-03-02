# Stubs for google.ads.google_ads.v6.proto.services.feed_mapping_service_pb2_grpc (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class FeedMappingServiceStub:
    GetFeedMapping: Any = ...
    MutateFeedMappings: Any = ...
    def __init__(self, channel: Any) -> None: ...

class FeedMappingServiceServicer:
    def GetFeedMapping(self, request: Any, context: Any) -> None: ...
    def MutateFeedMappings(self, request: Any, context: Any) -> None: ...

def add_FeedMappingServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class FeedMappingService:
    @staticmethod
    def GetFeedMapping(
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
    def MutateFeedMappings(
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