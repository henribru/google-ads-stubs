import grpc  # type: ignore
from google.ads.google_ads.v2.services.transports.keyword_plan_ad_group_service_grpc_transport import (
    KeywordPlanAdGroupServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v2.proto.resources.keyword_plan_ad_group_pb2 import (
    KeywordPlanAdGroup,
)
from google.ads.google_ads.v2.proto.services.keyword_plan_ad_group_service_pb2 import (
    KeywordPlanAdGroupOperation,
    MutateKeywordPlanAdGroupsResponse,
)

class KeywordPlanAdGroupServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> KeywordPlanAdGroupServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> KeywordPlanAdGroupServiceClient: ...
    @classmethod
    def keyword_plan_ad_group_path(
        cls, customer: Any, keyword_plan_ad_group: Any
    ) -> str: ...
    transport: Union[
        KeywordPlanAdGroupServiceGrpcTransport,
        Callable[[Credentials, type], KeywordPlanAdGroupServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                KeywordPlanAdGroupServiceGrpcTransport,
                Callable[[Credentials, type], KeywordPlanAdGroupServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_keyword_plan_ad_group(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> KeywordPlanAdGroup: ...
    def mutate_keyword_plan_ad_groups(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], KeywordPlanAdGroupOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateKeywordPlanAdGroupsResponse: ...
