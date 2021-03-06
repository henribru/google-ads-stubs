from typing import Any

class FeedServiceStub:
    GetFeed: Any = ...
    MutateFeeds: Any = ...
    def __init__(self, channel: Any) -> None: ...

class FeedServiceServicer:
    def GetFeed(self, request: Any, context: Any) -> None: ...
    def MutateFeeds(self, request: Any, context: Any) -> None: ...

def add_FeedServiceServicer_to_server(servicer: Any, server: Any) -> None: ...
