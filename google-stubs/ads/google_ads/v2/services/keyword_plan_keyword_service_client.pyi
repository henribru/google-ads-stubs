from typing import Any, Callable, ClassVar, Dict, List, Optional, Sequence, Tuple, Union

import grpc  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from google.auth.credentials import Credentials  # type: ignore

from google.ads.google_ads.v2.proto.resources.keyword_plan_keyword_pb2 import (
    KeywordPlanKeyword,
)
from google.ads.google_ads.v2.proto.services.keyword_plan_keyword_service_pb2 import (
    KeywordPlanKeywordOperation,
    MutateKeywordPlanKeywordsResponse,
)
from google.ads.google_ads.v2.services.transports.keyword_plan_keyword_service_grpc_transport import (
    KeywordPlanKeywordServiceGrpcTransport,
)

class KeywordPlanKeywordServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> KeywordPlanKeywordServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> KeywordPlanKeywordServiceClient: ...
    @classmethod
    def keyword_plan_keyword_path(
        cls, customer: Any, keyword_plan_keyword: Any
    ) -> str: ...
    transport: Union[
        KeywordPlanKeywordServiceGrpcTransport,
        Callable[[Credentials, type], KeywordPlanKeywordServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                KeywordPlanKeywordServiceGrpcTransport,
                Callable[[Credentials, type], KeywordPlanKeywordServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_keyword_plan_keyword(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> KeywordPlanKeyword: ...
    def mutate_keyword_plan_keywords(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], KeywordPlanKeywordOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateKeywordPlanKeywordsResponse: ...
