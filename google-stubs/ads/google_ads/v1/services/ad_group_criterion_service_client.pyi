import grpc  # type: ignore
from google.ads.google_ads.v1.services.transports.ad_group_criterion_service_grpc_transport import (
    AdGroupCriterionServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v1.proto.resources.ad_group_criterion_pb2 import (
    AdGroupCriterion,
)
from google.ads.google_ads.v1.proto.services.ad_group_criterion_service_pb2 import (
    AdGroupCriterionOperation,
    MutateAdGroupCriteriaResponse,
)

class AdGroupCriterionServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AdGroupCriterionServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AdGroupCriterionServiceClient: ...
    @classmethod
    def ad_group_criteria_path(cls, customer: Any, ad_group_criteria: Any) -> str: ...
    transport: Union[
        AdGroupCriterionServiceGrpcTransport,
        Callable[[Credentials, type], AdGroupCriterionServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                AdGroupCriterionServiceGrpcTransport,
                Callable[[Credentials, type], AdGroupCriterionServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_ad_group_criterion(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> AdGroupCriterion: ...
    def mutate_ad_group_criteria(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], AdGroupCriterionOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateAdGroupCriteriaResponse: ...
