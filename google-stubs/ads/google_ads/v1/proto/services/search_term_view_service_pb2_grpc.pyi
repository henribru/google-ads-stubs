# Stubs for google.ads.google_ads.v1.proto.services.search_term_view_service_pb2_grpc (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class SearchTermViewServiceStub:
    GetSearchTermView: Any = ...
    def __init__(self, channel: Any) -> None: ...

class SearchTermViewServiceServicer:
    def GetSearchTermView(self, request: Any, context: Any) -> None: ...

def add_SearchTermViewServiceServicer_to_server(servicer: Any, server: Any) -> None: ...