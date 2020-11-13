# Stubs for google.ads.google_ads.v6.proto.services.feed_item_set_service_pb2_grpc (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class FeedItemSetServiceStub:
    GetFeedItemSet: Any = ...
    MutateFeedItemSets: Any = ...
    def __init__(self, channel: Any) -> None: ...

class FeedItemSetServiceServicer:
    def GetFeedItemSet(self, request: Any, context: Any) -> None: ...
    def MutateFeedItemSets(self, request: Any, context: Any) -> None: ...

def add_FeedItemSetServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class FeedItemSetService:
    @staticmethod
    def GetFeedItemSet(
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
    def MutateFeedItemSets(
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
