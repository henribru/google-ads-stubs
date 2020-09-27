from typing import Any, Callable, ClassVar, Dict, List, Optional, Sequence, Tuple, Union

import grpc  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from google.auth.credentials import Credentials  # type: ignore

from google.ads.google_ads.v2.proto.resources.customer_negative_criterion_pb2 import (
    CustomerNegativeCriterion,
)
from google.ads.google_ads.v2.proto.services.customer_negative_criterion_service_pb2 import (
    CustomerNegativeCriterionOperation,
    MutateCustomerNegativeCriteriaResponse,
)
from google.ads.google_ads.v2.services.transports.customer_negative_criterion_service_grpc_transport import (
    CustomerNegativeCriterionServiceGrpcTransport,
)

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
        CustomerNegativeCriterionServiceGrpcTransport,
        Callable[[Credentials, type], CustomerNegativeCriterionServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                CustomerNegativeCriterionServiceGrpcTransport,
                Callable[
                    [Credentials, type], CustomerNegativeCriterionServiceGrpcTransport
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
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
        operations: List[Union[Dict[str, Any], CustomerNegativeCriterionOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateCustomerNegativeCriteriaResponse: ...
