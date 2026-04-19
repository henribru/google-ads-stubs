import abc
from typing import Awaitable, Callable, Sequence

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v23.services.types import reservation_service

__all__ = ["ReservationServiceTransport"]

class ReservationServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(
        self,
        *,
        host: str = "googleads.googleapis.com",
        credentials: ga_credentials.Credentials | None = None,
        credentials_file: str | None = None,
        scopes: Sequence[str] | None = None,
        quota_project_id: str | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: bool | None = False,
        api_audience: str | None = None,
        **kwargs,
    ) -> None: ...
    @property
    def host(self): ...
    def close(self) -> None: ...
    @property
    def quote_campaigns(
        self,
    ) -> Callable[
        [reservation_service.QuoteCampaignsRequest],
        reservation_service.QuoteCampaignsResponse
        | Awaitable[reservation_service.QuoteCampaignsResponse],
    ]: ...
    @property
    def book_campaigns(
        self,
    ) -> Callable[
        [reservation_service.BookCampaignsRequest],
        reservation_service.BookCampaignsResponse
        | Awaitable[reservation_service.BookCampaignsResponse],
    ]: ...
    @property
    def kind(self) -> str: ...
