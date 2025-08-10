import abc
from typing import Awaitable, Callable, Sequence

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v21.services.types import campaign_service

__all__ = ["CampaignServiceTransport"]

class CampaignServiceTransport(abc.ABC):
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
    def mutate_campaigns(
        self,
    ) -> Callable[
        [campaign_service.MutateCampaignsRequest],
        campaign_service.MutateCampaignsResponse
        | Awaitable[campaign_service.MutateCampaignsResponse],
    ]: ...
    @property
    def enable_p_max_brand_guidelines(
        self,
    ) -> Callable[
        [campaign_service.EnablePMaxBrandGuidelinesRequest],
        campaign_service.EnablePMaxBrandGuidelinesResponse
        | Awaitable[campaign_service.EnablePMaxBrandGuidelinesResponse],
    ]: ...
    @property
    def kind(self) -> str: ...
