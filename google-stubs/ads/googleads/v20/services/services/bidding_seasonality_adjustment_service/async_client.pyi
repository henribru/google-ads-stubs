from .transports.base import BiddingSeasonalityAdjustmentServiceTransport
from _typeshed import Incomplete
from google.ads.googleads.v20.services.types import bidding_seasonality_adjustment_service
from google.api_core import gapic_v1, retry_async as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials
from typing import Callable, MutableSequence, Sequence, Tuple

__all__ = ['BiddingSeasonalityAdjustmentServiceAsyncClient']

class BiddingSeasonalityAdjustmentServiceAsyncClient:
    DEFAULT_ENDPOINT: Incomplete
    DEFAULT_MTLS_ENDPOINT: Incomplete
    bidding_seasonality_adjustment_path: Incomplete
    parse_bidding_seasonality_adjustment_path: Incomplete
    campaign_path: Incomplete
    parse_campaign_path: Incomplete
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
    def get_mtls_endpoint_and_cert_source(cls, client_options: ClientOptions | None = None): ...
    @property
    def transport(self) -> BiddingSeasonalityAdjustmentServiceTransport: ...
    @property
    def api_endpoint(self): ...
    @property
    def universe_domain(self) -> str: ...
    get_transport_class: Incomplete
    def __init__(self, *, credentials: ga_credentials.Credentials | None = None, transport: str | BiddingSeasonalityAdjustmentServiceTransport | Callable[..., BiddingSeasonalityAdjustmentServiceTransport] | None = 'grpc_asyncio', client_options: ClientOptions | None = None, client_info: gapic_v1.client_info.ClientInfo = ...) -> None: ...
    async def mutate_bidding_seasonality_adjustments(self, request: bidding_seasonality_adjustment_service.MutateBiddingSeasonalityAdjustmentsRequest | dict | None = None, *, customer_id: str | None = None, operations: MutableSequence[bidding_seasonality_adjustment_service.BiddingSeasonalityAdjustmentOperation] | None = None, retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ..., timeout: float | object = ..., metadata: Sequence[Tuple[str, str | bytes]] = ()) -> bidding_seasonality_adjustment_service.MutateBiddingSeasonalityAdjustmentsResponse: ...
    async def __aenter__(self) -> BiddingSeasonalityAdjustmentServiceAsyncClient: ...
    async def __aexit__(self, exc_type, exc, tb) -> None: ...
