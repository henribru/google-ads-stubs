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

from google.ads.google_ads.v4.proto.services import (
    keyword_plan_idea_service_pb2 as keyword_plan_idea_service_pb2,
)
from google.ads.google_ads.v4.services import (
    keyword_plan_idea_service_client_config as keyword_plan_idea_service_client_config,
)
from google.ads.google_ads.v4.services.transports import (
    keyword_plan_idea_service_grpc_transport as keyword_plan_idea_service_grpc_transport,
)
from google.ads.google_ads.v4.types import (
    GenerateKeywordIdeaResult,
    KeywordAndUrlSeed,
    KeywordPlanNetworkEnum,
    KeywordSeed,
    SiteSeed,
    StringValue,
    UrlSeed,
)

class KeywordPlanIdeaServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> KeywordPlanIdeaServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> KeywordPlanIdeaServiceClient: ...
    transport: Union[
        keyword_plan_idea_service_grpc_transport.KeywordPlanIdeaServiceGrpcTransport,
        Callable[
            [Credentials, type],
            keyword_plan_idea_service_grpc_transport.KeywordPlanIdeaServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                keyword_plan_idea_service_grpc_transport.KeywordPlanIdeaServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    keyword_plan_idea_service_grpc_transport.KeywordPlanIdeaServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def generate_keyword_ideas(
        self,
        customer_id: str,
        language: Union[Dict[str, Any], StringValue],
        geo_target_constants: List[Union[Dict[str, Any], StringValue]],
        include_adult_keywords: bool,
        keyword_plan_network: KeywordPlanNetworkEnum.KeywordPlanNetworkValue,
        page_size: Optional[int] = ...,
        keyword_and_url_seed: Optional[Union[Dict[str, Any], KeywordAndUrlSeed]] = ...,
        keyword_seed: Optional[Union[Dict[str, Any], KeywordSeed]] = ...,
        url_seed: Optional[Union[Dict[str, Any], UrlSeed]] = ...,
        site_seed: Optional[Union[Dict[str, Any], SiteSeed]] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> Iterable[GenerateKeywordIdeaResult]: ...
