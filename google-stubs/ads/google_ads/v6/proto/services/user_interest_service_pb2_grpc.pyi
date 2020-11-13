# Stubs for google.ads.google_ads.v6.proto.services.user_interest_service_pb2_grpc (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class UserInterestServiceStub:
    GetUserInterest: Any = ...
    def __init__(self, channel: Any) -> None: ...

class UserInterestServiceServicer:
    def GetUserInterest(self, request: Any, context: Any) -> None: ...

def add_UserInterestServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class UserInterestService:
    @staticmethod
    def GetUserInterest(
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
