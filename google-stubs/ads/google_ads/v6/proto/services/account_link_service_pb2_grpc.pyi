# Stubs for google.ads.google_ads.v6.proto.services.account_link_service_pb2_grpc (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class AccountLinkServiceStub:
    GetAccountLink: Any = ...
    CreateAccountLink: Any = ...
    MutateAccountLink: Any = ...
    def __init__(self, channel: Any) -> None: ...

class AccountLinkServiceServicer:
    def GetAccountLink(self, request: Any, context: Any) -> None: ...
    def CreateAccountLink(self, request: Any, context: Any) -> None: ...
    def MutateAccountLink(self, request: Any, context: Any) -> None: ...

def add_AccountLinkServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class AccountLinkService:
    @staticmethod
    def GetAccountLink(
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
    def CreateAccountLink(
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
    def MutateAccountLink(
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
