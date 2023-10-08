import abc
from typing import Awaitable, Callable, Optional, Sequence, Union

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v14.services.types import smart_campaign_setting_service

class SmartCampaignSettingServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: Optional[ga_credentials.Credentials] = ...,
        credentials_file: Optional[str] = ...,
        scopes: Optional[Sequence[str]] = ...,
        quota_project_id: Optional[str] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: Optional[bool] = ...,
        **kwargs
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def get_smart_campaign_status(
        self,
    ) -> Callable[
        [smart_campaign_setting_service.GetSmartCampaignStatusRequest],
        Union[
            smart_campaign_setting_service.GetSmartCampaignStatusResponse,
            Awaitable[smart_campaign_setting_service.GetSmartCampaignStatusResponse],
        ],
    ]: ...
    @property
    def mutate_smart_campaign_settings(
        self,
    ) -> Callable[
        [smart_campaign_setting_service.MutateSmartCampaignSettingsRequest],
        Union[
            smart_campaign_setting_service.MutateSmartCampaignSettingsResponse,
            Awaitable[
                smart_campaign_setting_service.MutateSmartCampaignSettingsResponse
            ],
        ],
    ]: ...