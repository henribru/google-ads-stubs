# Stubs for google.ads.google_ads.v1.proto.services.ad_group_feed_service_pb2_grpc (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class AdGroupFeedServiceStub:
    GetAdGroupFeed: Any = ...
    MutateAdGroupFeeds: Any = ...
    def __init__(self, channel: Any) -> None: ...

class AdGroupFeedServiceServicer:
    def GetAdGroupFeed(self, request: Any, context: Any) -> None: ...
    def MutateAdGroupFeeds(self, request: Any, context: Any) -> None: ...

def add_AdGroupFeedServiceServicer_to_server(servicer: Any, server: Any) -> None: ...