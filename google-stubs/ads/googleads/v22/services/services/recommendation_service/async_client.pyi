from typing import Callable, MutableSequence, Sequence

from _typeshed import Incomplete
from google.api_core import gapic_v1, retry_async as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials

from google.ads.googleads.v22.enums.types import (
    advertising_channel_type as gage_advertising_channel_type,
    recommendation_type,
)
from google.ads.googleads.v22.services.types import recommendation_service

from .transports.base import RecommendationServiceTransport

__all__ = ["RecommendationServiceAsyncClient"]

class RecommendationServiceAsyncClient:
    DEFAULT_ENDPOINT: Incomplete
    DEFAULT_MTLS_ENDPOINT: Incomplete
    ad_path: Incomplete
    parse_ad_path: Incomplete
    ad_group_path: Incomplete
    parse_ad_group_path: Incomplete
    asset_path: Incomplete
    parse_asset_path: Incomplete
    campaign_path: Incomplete
    parse_campaign_path: Incomplete
    campaign_budget_path: Incomplete
    parse_campaign_budget_path: Incomplete
    conversion_action_path: Incomplete
    parse_conversion_action_path: Incomplete
    recommendation_path: Incomplete
    parse_recommendation_path: Incomplete
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
    def transport(self) -> RecommendationServiceTransport: ...
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
        | RecommendationServiceTransport
        | Callable[..., RecommendationServiceTransport]
        | None = "grpc_asyncio",
        client_options: ClientOptions | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
    ) -> None: ...
    async def apply_recommendation(
        self,
        request: recommendation_service.ApplyRecommendationRequest | dict | None = None,
        *,
        customer_id: str | None = None,
        operations: MutableSequence[recommendation_service.ApplyRecommendationOperation]
        | None = None,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> recommendation_service.ApplyRecommendationResponse: ...
    async def dismiss_recommendation(
        self,
        request: recommendation_service.DismissRecommendationRequest
        | dict
        | None = None,
        *,
        customer_id: str | None = None,
        operations: MutableSequence[
            recommendation_service.DismissRecommendationRequest.DismissRecommendationOperation
        ]
        | None = None,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> recommendation_service.DismissRecommendationResponse: ...
    async def generate_recommendations(
        self,
        request: recommendation_service.GenerateRecommendationsRequest
        | dict
        | None = None,
        *,
        customer_id: str | None = None,
        recommendation_types: MutableSequence[
            recommendation_type.RecommendationTypeEnum.RecommendationType
        ]
        | None = None,
        advertising_channel_type: gage_advertising_channel_type.AdvertisingChannelTypeEnum.AdvertisingChannelType
        | None = None,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> recommendation_service.GenerateRecommendationsResponse: ...
    async def __aenter__(self) -> RecommendationServiceAsyncClient: ...
    async def __aexit__(self, exc_type, exc, tb) -> None: ...
