from google.ads.google_ads.v3.proto.services import (
    keyword_plan_idea_service_pb2 as keyword_plan_idea_service_pb2,
)
from google.ads.google_ads.v3.services import (
    keyword_plan_idea_service_client_config as keyword_plan_idea_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    keyword_plan_idea_service_grpc_transport as keyword_plan_idea_service_grpc_transport,
)
from google.oauth2 import service_account as service_account  # type: ignore
import grpc  # type: ignore
from google.ads.google_ads.v3.services.transports.keyword_plan_idea_service_grpc_transport import (
    KeywordPlanIdeaServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import (
    Optional,
    Dict,
    Any,
    List,
    Sequence,
    Tuple,
    Union,
    Callable,
    ClassVar,
    Text,
)
from typing_extensions import TypedDict
from google.ads.google_ads.v3.types import (
    StringValue,
    KeywordPlanNetworkEnum,
    KeywordAndUrlSeed,
    KeywordSeed,
    UrlSeed,
    GenerateKeywordIdeaResponse,
)

class StringValueDict(TypedDict):
    value: Text

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
        KeywordPlanIdeaServiceGrpcTransport,
        Callable[[Credentials, type], KeywordPlanIdeaServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                KeywordPlanIdeaServiceGrpcTransport,
                Callable[[Credentials, type], KeywordPlanIdeaServiceGrpcTransport],
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
        language: Union[StringValueDict, StringValue],
        geo_target_constants: List[Union[StringValueDict, StringValue]],
        keyword_plan_network: KeywordPlanNetworkEnum.KeywordPlanNetwork,
        keyword_and_url_seed: Optional[Union[Dict[str, Any], KeywordAndUrlSeed]] = ...,
        keyword_seed: Optional[Union[Dict[str, Any], KeywordSeed]] = ...,
        url_seed: Optional[Union[Dict[str, Any], UrlSeed]] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> GenerateKeywordIdeaResponse: ...
