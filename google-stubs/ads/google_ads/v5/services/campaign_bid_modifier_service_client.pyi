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

from google.ads.google_ads.v5.proto.services import (
    campaign_bid_modifier_service_pb2 as campaign_bid_modifier_service_pb2,
)
from google.ads.google_ads.v5.services import (
    campaign_bid_modifier_service_client_config as campaign_bid_modifier_service_client_config,
)
from google.ads.google_ads.v5.services.transports import (
    campaign_bid_modifier_service_grpc_transport as campaign_bid_modifier_service_grpc_transport,
)
from google.ads.google_ads.v5.types import CampaignBidModifier

class CampaignBidModifierServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CampaignBidModifierServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CampaignBidModifierServiceClient: ...
    @classmethod
    def campaign_bid_modifier_path(
        cls, customer: Any, campaign_bid_modifier: Any
    ) -> str: ...
    transport: Union[
        campaign_bid_modifier_service_grpc_transport.CampaignBidModifierServiceGrpcTransport,
        Callable[
            [Credentials, type],
            campaign_bid_modifier_service_grpc_transport.CampaignBidModifierServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                campaign_bid_modifier_service_grpc_transport.CampaignBidModifierServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    campaign_bid_modifier_service_grpc_transport.CampaignBidModifierServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
        client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    ) -> None: ...
    def get_campaign_bid_modifier(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> CampaignBidModifier: ...
    def mutate_campaign_bid_modifiers(
        self,
        customer_id: str,
        operations: List[
            Union[
                Dict[str, Any],
                campaign_bid_modifier_service_pb2.CampaignBidModifierOperation,
            ]
        ],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> campaign_bid_modifier_service_pb2.MutateCampaignBidModifiersResponse: ...
