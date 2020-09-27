from typing import (
    Any,
    Callable,
    ClassVar,
    Dict,
    Iterable,
    List,
    Optional,
    Sequence,
    Tuple,
    Union,
)

import grpc  # type: ignore
from google.api_core.client_options import ClientOptions  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from google.auth.credentials import Credentials  # type: ignore
from google.oauth2 import service_account as service_account  # type: ignore

from google.ads.google_ads.v2.proto.resources import (
    account_budget_pb2 as account_budget_pb2,
    account_budget_proposal_pb2 as account_budget_proposal_pb2,
    ad_group_ad_asset_view_pb2 as ad_group_ad_asset_view_pb2,
    ad_group_ad_label_pb2 as ad_group_ad_label_pb2,
    ad_group_ad_pb2 as ad_group_ad_pb2,
    ad_group_audience_view_pb2 as ad_group_audience_view_pb2,
    ad_group_bid_modifier_pb2 as ad_group_bid_modifier_pb2,
    ad_group_criterion_label_pb2 as ad_group_criterion_label_pb2,
    ad_group_criterion_pb2 as ad_group_criterion_pb2,
    ad_group_criterion_simulation_pb2 as ad_group_criterion_simulation_pb2,
    ad_group_extension_setting_pb2 as ad_group_extension_setting_pb2,
    ad_group_feed_pb2 as ad_group_feed_pb2,
    ad_group_label_pb2 as ad_group_label_pb2,
    ad_group_pb2 as ad_group_pb2,
    ad_group_simulation_pb2 as ad_group_simulation_pb2,
    ad_parameter_pb2 as ad_parameter_pb2,
    ad_pb2 as ad_pb2,
    ad_schedule_view_pb2 as ad_schedule_view_pb2,
    age_range_view_pb2 as age_range_view_pb2,
    asset_pb2 as asset_pb2,
)
from google.ads.google_ads.v2.proto.services import (
    account_budget_proposal_service_pb2 as account_budget_proposal_service_pb2,
    account_budget_proposal_service_pb2_grpc as account_budget_proposal_service_pb2_grpc,
    account_budget_service_pb2 as account_budget_service_pb2,
    account_budget_service_pb2_grpc as account_budget_service_pb2_grpc,
    ad_group_ad_asset_view_service_pb2 as ad_group_ad_asset_view_service_pb2,
    ad_group_ad_asset_view_service_pb2_grpc as ad_group_ad_asset_view_service_pb2_grpc,
    ad_group_ad_label_service_pb2 as ad_group_ad_label_service_pb2,
    ad_group_ad_label_service_pb2_grpc as ad_group_ad_label_service_pb2_grpc,
    ad_group_ad_service_pb2 as ad_group_ad_service_pb2,
    ad_group_ad_service_pb2_grpc as ad_group_ad_service_pb2_grpc,
    ad_group_audience_view_service_pb2 as ad_group_audience_view_service_pb2,
    ad_group_audience_view_service_pb2_grpc as ad_group_audience_view_service_pb2_grpc,
    ad_group_bid_modifier_service_pb2 as ad_group_bid_modifier_service_pb2,
    ad_group_bid_modifier_service_pb2_grpc as ad_group_bid_modifier_service_pb2_grpc,
    ad_group_criterion_label_service_pb2 as ad_group_criterion_label_service_pb2,
    ad_group_criterion_label_service_pb2_grpc as ad_group_criterion_label_service_pb2_grpc,
    ad_group_criterion_service_pb2 as ad_group_criterion_service_pb2,
    ad_group_criterion_service_pb2_grpc as ad_group_criterion_service_pb2_grpc,
    ad_group_criterion_simulation_service_pb2 as ad_group_criterion_simulation_service_pb2,
    ad_group_criterion_simulation_service_pb2_grpc as ad_group_criterion_simulation_service_pb2_grpc,
    ad_group_extension_setting_service_pb2 as ad_group_extension_setting_service_pb2,
    ad_group_extension_setting_service_pb2_grpc as ad_group_extension_setting_service_pb2_grpc,
    ad_group_feed_service_pb2 as ad_group_feed_service_pb2,
    ad_group_feed_service_pb2_grpc as ad_group_feed_service_pb2_grpc,
    ad_group_label_service_pb2 as ad_group_label_service_pb2,
    ad_group_label_service_pb2_grpc as ad_group_label_service_pb2_grpc,
    ad_group_service_pb2 as ad_group_service_pb2,
    ad_group_service_pb2_grpc as ad_group_service_pb2_grpc,
    ad_group_simulation_service_pb2 as ad_group_simulation_service_pb2,
    ad_group_simulation_service_pb2_grpc as ad_group_simulation_service_pb2_grpc,
    ad_parameter_service_pb2 as ad_parameter_service_pb2,
    ad_parameter_service_pb2_grpc as ad_parameter_service_pb2_grpc,
    ad_schedule_view_service_pb2 as ad_schedule_view_service_pb2,
    ad_schedule_view_service_pb2_grpc as ad_schedule_view_service_pb2_grpc,
    ad_service_pb2 as ad_service_pb2,
    ad_service_pb2_grpc as ad_service_pb2_grpc,
    age_range_view_service_pb2 as age_range_view_service_pb2,
    age_range_view_service_pb2_grpc as age_range_view_service_pb2_grpc,
    asset_service_pb2 as asset_service_pb2,
    asset_service_pb2_grpc as asset_service_pb2_grpc,
)
from google.ads.google_ads.v2.services import (
    asset_service_client_config as asset_service_client_config,
    enums as enums,
)
from google.ads.google_ads.v2.services.transports import (
    asset_service_grpc_transport as asset_service_grpc_transport,
)
from google.ads.google_ads.v2.types import Asset

class AssetServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AssetServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AssetServiceClient: ...
    @classmethod
    def asset_path(cls, customer: Any, asset: Any) -> str: ...
    transport: Union[
        asset_service_grpc_transport.AssetServiceGrpcTransport,
        Callable[
            [Credentials, type], asset_service_grpc_transport.AssetServiceGrpcTransport
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                asset_service_grpc_transport.AssetServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    asset_service_grpc_transport.AssetServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_asset(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> Asset: ...
    def mutate_assets(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], asset_service_pb2.AssetOperation]],
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> asset_service_pb2.MutateAssetsResponse: ...
