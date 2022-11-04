import abc
from typing import Awaitable, Callable, Optional, Sequence, Union

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v12.services.types import campaign_shared_set_service

class CampaignSharedSetServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        credentials_file: Optional[str] = ...,
        scopes: Optional[Sequence[str]] = ...,
        quota_project_id: Optional[str] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: Optional[bool] = ...,
        **kwargs
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def mutate_campaign_shared_sets(
        self,
    ) -> Callable[
        [campaign_shared_set_service.MutateCampaignSharedSetsRequest],
        Union[
            campaign_shared_set_service.MutateCampaignSharedSetsResponse,
            Awaitable[campaign_shared_set_service.MutateCampaignSharedSetsResponse],
        ],
    ]: ...
