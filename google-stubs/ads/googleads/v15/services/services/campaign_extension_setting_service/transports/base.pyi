import abc
from typing import Awaitable, Callable, Sequence

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v15.services.types import campaign_extension_setting_service

__all__ = ["CampaignExtensionSettingServiceTransport"]

class CampaignExtensionSettingServiceTransport(abc.ABC):
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
    def mutate_campaign_extension_settings(
        self,
    ) -> Callable[
        [campaign_extension_setting_service.MutateCampaignExtensionSettingsRequest],
        campaign_extension_setting_service.MutateCampaignExtensionSettingsResponse
        | Awaitable[
            campaign_extension_setting_service.MutateCampaignExtensionSettingsResponse
        ],
    ]: ...
