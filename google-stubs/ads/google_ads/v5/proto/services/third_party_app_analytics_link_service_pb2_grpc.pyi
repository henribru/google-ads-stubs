from typing import Any, Optional

class ThirdPartyAppAnalyticsLinkServiceStub:
    GetThirdPartyAppAnalyticsLink: Any = ...
    RegenerateShareableLinkId: Any = ...
    def __init__(self, channel: Any) -> None: ...

class ThirdPartyAppAnalyticsLinkServiceServicer:
    def GetThirdPartyAppAnalyticsLink(self, request: Any, context: Any) -> None: ...
    def RegenerateShareableLinkId(self, request: Any, context: Any) -> None: ...

def add_ThirdPartyAppAnalyticsLinkServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class ThirdPartyAppAnalyticsLinkService:
    @staticmethod
    def GetThirdPartyAppAnalyticsLink(
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
    def RegenerateShareableLinkId(
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
