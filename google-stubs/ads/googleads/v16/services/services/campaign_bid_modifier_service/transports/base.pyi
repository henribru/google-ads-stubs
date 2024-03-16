import abc
from typing import Awaitable, Callable, Sequence

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v16.services.types import campaign_bid_modifier_service

__all__ = ["CampaignBidModifierServiceTransport"]

class CampaignBidModifierServiceTransport(abc.ABC):
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
        **kwargs,
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def mutate_campaign_bid_modifiers(
        self,
    ) -> Callable[
        [campaign_bid_modifier_service.MutateCampaignBidModifiersRequest],
        campaign_bid_modifier_service.MutateCampaignBidModifiersResponse
        | Awaitable[campaign_bid_modifier_service.MutateCampaignBidModifiersResponse],
    ]: ...
