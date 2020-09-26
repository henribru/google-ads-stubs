from typing import Any, Optional

class MerchantCenterLinkServiceStub:
    ListMerchantCenterLinks: Any = ...
    GetMerchantCenterLink: Any = ...
    MutateMerchantCenterLink: Any = ...
    def __init__(self, channel: Any) -> None: ...

class MerchantCenterLinkServiceServicer:
    def ListMerchantCenterLinks(self, request: Any, context: Any) -> None: ...
    def GetMerchantCenterLink(self, request: Any, context: Any) -> None: ...
    def MutateMerchantCenterLink(self, request: Any, context: Any) -> None: ...

def add_MerchantCenterLinkServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class MerchantCenterLinkService:
    @staticmethod
    def ListMerchantCenterLinks(
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
    def GetMerchantCenterLink(
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
    def MutateMerchantCenterLink(
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
