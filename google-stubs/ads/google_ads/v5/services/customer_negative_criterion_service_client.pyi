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
    customer_negative_criterion_service_pb2 as customer_negative_criterion_service_pb2,
)
from google.ads.google_ads.v5.services import (
    customer_negative_criterion_service_client_config as customer_negative_criterion_service_client_config,
)
from google.ads.google_ads.v5.services.transports import (
    customer_negative_criterion_service_grpc_transport as customer_negative_criterion_service_grpc_transport,
)
from google.ads.google_ads.v5.types import CustomerNegativeCriterion

class CustomerNegativeCriterionServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CustomerNegativeCriterionServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CustomerNegativeCriterionServiceClient: ...
    @classmethod
    def customer_negative_criteria_path(
        cls, customer: Any, customer_negative_criteria: Any
    ) -> str: ...
    transport: Union[
        customer_negative_criterion_service_grpc_transport.CustomerNegativeCriterionServiceGrpcTransport,
        Callable[
            [Credentials, type],
            customer_negative_criterion_service_grpc_transport.CustomerNegativeCriterionServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                customer_negative_criterion_service_grpc_transport.CustomerNegativeCriterionServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    customer_negative_criterion_service_grpc_transport.CustomerNegativeCriterionServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
        client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    ) -> None: ...
    def get_customer_negative_criterion(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> CustomerNegativeCriterion: ...
    def mutate_customer_negative_criteria(
        self,
        customer_id: str,
        operations: List[
            Union[
                Dict[str, Any],
                customer_negative_criterion_service_pb2.CustomerNegativeCriterionOperation,
            ]
        ],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> customer_negative_criterion_service_pb2.MutateCustomerNegativeCriteriaResponse: ...
