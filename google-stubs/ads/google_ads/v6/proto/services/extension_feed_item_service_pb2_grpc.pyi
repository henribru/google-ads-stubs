# Stubs for google.ads.google_ads.v6.proto.services.extension_feed_item_service_pb2_grpc (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class ExtensionFeedItemServiceStub:
    GetExtensionFeedItem: Any = ...
    MutateExtensionFeedItems: Any = ...
    def __init__(self, channel: Any) -> None: ...

class ExtensionFeedItemServiceServicer:
    def GetExtensionFeedItem(self, request: Any, context: Any) -> None: ...
    def MutateExtensionFeedItems(self, request: Any, context: Any) -> None: ...

def add_ExtensionFeedItemServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class ExtensionFeedItemService:
    @staticmethod
    def GetExtensionFeedItem(
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
    def MutateExtensionFeedItems(
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
