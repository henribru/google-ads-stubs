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

import grpc
from google.api_core.client_options import ClientOptions  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from google.auth.credentials import Credentials  # type: ignore
from google.oauth2 import service_account as service_account  # type: ignore

from google.ads.google_ads.v5.proto.services import (
    ad_group_criterion_label_service_pb2 as ad_group_criterion_label_service_pb2,
)
from google.ads.google_ads.v5.services import (
    ad_group_criterion_label_service_client_config as ad_group_criterion_label_service_client_config,
)
from google.ads.google_ads.v5.services.transports import (
    ad_group_criterion_label_service_grpc_transport as ad_group_criterion_label_service_grpc_transport,
)
from google.ads.google_ads.v5.types import AdGroupCriterionLabel

class AdGroupCriterionLabelServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AdGroupCriterionLabelServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AdGroupCriterionLabelServiceClient: ...
    @classmethod
    def ad_group_criterion_label_path(
        cls, customer: Any, ad_group_criterion_label: Any
    ) -> str: ...
    transport: Union[
        ad_group_criterion_label_service_grpc_transport.AdGroupCriterionLabelServiceGrpcTransport,
        Callable[
            [Credentials, type],
            ad_group_criterion_label_service_grpc_transport.AdGroupCriterionLabelServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                ad_group_criterion_label_service_grpc_transport.AdGroupCriterionLabelServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    ad_group_criterion_label_service_grpc_transport.AdGroupCriterionLabelServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
        client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    ) -> None: ...
    def get_ad_group_criterion_label(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> AdGroupCriterionLabel: ...
    def mutate_ad_group_criterion_labels(
        self,
        customer_id: str,
        operations: List[
            Union[
                Dict[str, Any],
                ad_group_criterion_label_service_pb2.AdGroupCriterionLabelOperation,
            ]
        ],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> ad_group_criterion_label_service_pb2.MutateAdGroupCriterionLabelsResponse: ...
