import abc
from typing import Awaitable, Callable, Optional, Sequence, Union

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v10.services.types import (
    third_party_app_analytics_link_service,
)

class ThirdPartyAppAnalyticsLinkServiceTransport(abc.ABC):
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
    def regenerate_shareable_link_id(
        self,
    ) -> Callable[
        [third_party_app_analytics_link_service.RegenerateShareableLinkIdRequest],
        Union[
            third_party_app_analytics_link_service.RegenerateShareableLinkIdResponse,
            Awaitable[
                third_party_app_analytics_link_service.RegenerateShareableLinkIdResponse
            ],
        ],
    ]: ...
