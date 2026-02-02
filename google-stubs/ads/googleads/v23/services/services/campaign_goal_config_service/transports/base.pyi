import abc
from _typeshed import Incomplete
from google.ads.googleads.v23.services.types import campaign_goal_config_service
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials
from typing import Awaitable, Callable, Sequence

__all__ = ['CampaignGoalConfigServiceTransport']

class CampaignGoalConfigServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(self, *, host: str = 'googleads.googleapis.com', credentials: ga_credentials.Credentials | None = None, credentials_file: str | None = None, scopes: Sequence[str] | None = None, quota_project_id: str | None = None, client_info: gapic_v1.client_info.ClientInfo = ..., always_use_jwt_access: bool | None = False, api_audience: str | None = None, **kwargs) -> None: ...
    @property
    def host(self): ...
    def close(self) -> None: ...
    @property
    def mutate_campaign_goal_configs(self) -> Callable[[campaign_goal_config_service.MutateCampaignGoalConfigsRequest], campaign_goal_config_service.MutateCampaignGoalConfigsResponse | Awaitable[campaign_goal_config_service.MutateCampaignGoalConfigsResponse]]: ...
    @property
    def kind(self) -> str: ...
