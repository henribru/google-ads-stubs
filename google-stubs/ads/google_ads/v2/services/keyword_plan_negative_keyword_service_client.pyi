import grpc  # type: ignore
from google.ads.google_ads.v2.services.transports.keyword_plan_negative_keyword_service_grpc_transport import (
    KeywordPlanNegativeKeywordServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v2.proto.resources.keyword_plan_negative_keyword_pb2 import (
    KeywordPlanNegativeKeyword,
)
from google.ads.google_ads.v2.proto.services.keyword_plan_negative_keyword_service_pb2 import (
    KeywordPlanNegativeKeywordOperation,
    MutateKeywordPlanNegativeKeywordsResponse,
)

class KeywordPlanNegativeKeywordServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> KeywordPlanNegativeKeywordServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> KeywordPlanNegativeKeywordServiceClient: ...
    @classmethod
    def keyword_plan_negative_keyword_path(
        cls, customer: Any, keyword_plan_negative_keyword: Any
    ) -> str: ...
    transport: Union[
        KeywordPlanNegativeKeywordServiceGrpcTransport,
        Callable[[Credentials, type], KeywordPlanNegativeKeywordServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                KeywordPlanNegativeKeywordServiceGrpcTransport,
                Callable[
                    [Credentials, type], KeywordPlanNegativeKeywordServiceGrpcTransport
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_keyword_plan_negative_keyword(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> KeywordPlanNegativeKeyword: ...
    def mutate_keyword_plan_negative_keywords(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], KeywordPlanNegativeKeywordOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateKeywordPlanNegativeKeywordsResponse: ...
