from typing import Callable, MutableSequence, Sequence, Tuple

from _typeshed import Incomplete
from google.api_core import gapic_v1, retry_async as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials

from google.ads.googleads.v18.services.types import campaign_criterion_service

from .transports.base import CampaignCriterionServiceTransport

__all__ = ["CampaignCriterionServiceAsyncClient"]

class CampaignCriterionServiceAsyncClient:
    DEFAULT_ENDPOINT: Incomplete
    DEFAULT_MTLS_ENDPOINT: Incomplete
    campaign_path: Incomplete
    parse_campaign_path: Incomplete
    campaign_criterion_path: Incomplete
    parse_campaign_criterion_path: Incomplete
    carrier_constant_path: Incomplete
    parse_carrier_constant_path: Incomplete
    combined_audience_path: Incomplete
    parse_combined_audience_path: Incomplete
    keyword_theme_constant_path: Incomplete
    parse_keyword_theme_constant_path: Incomplete
    mobile_app_category_constant_path: Incomplete
    parse_mobile_app_category_constant_path: Incomplete
    mobile_device_constant_path: Incomplete
    parse_mobile_device_constant_path: Incomplete
    operating_system_version_constant_path: Incomplete
    parse_operating_system_version_constant_path: Incomplete
    topic_constant_path: Incomplete
    parse_topic_constant_path: Incomplete
    common_billing_account_path: Incomplete
    parse_common_billing_account_path: Incomplete
    common_folder_path: Incomplete
    parse_common_folder_path: Incomplete
    common_organization_path: Incomplete
    parse_common_organization_path: Incomplete
    common_project_path: Incomplete
    parse_common_project_path: Incomplete
    common_location_path: Incomplete
    parse_common_location_path: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: ClientOptions | None = None
    ): ...
    @property
    def transport(self) -> CampaignCriterionServiceTransport: ...
    @property
    def api_endpoint(self): ...
    @property
    def universe_domain(self) -> str: ...
    get_transport_class: Incomplete
    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials | None = None,
        transport: str
        | CampaignCriterionServiceTransport
        | Callable[..., CampaignCriterionServiceTransport]
        | None = "grpc_asyncio",
        client_options: ClientOptions | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
    ) -> None: ...
    async def mutate_campaign_criteria(
        self,
        request: campaign_criterion_service.MutateCampaignCriteriaRequest
        | dict
        | None = None,
        *,
        customer_id: str | None = None,
        operations: MutableSequence[
            campaign_criterion_service.CampaignCriterionOperation
        ]
        | None = None,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> campaign_criterion_service.MutateCampaignCriteriaResponse: ...
    async def __aenter__(self) -> CampaignCriterionServiceAsyncClient: ...
    async def __aexit__(self, exc_type, exc, tb) -> None: ...
