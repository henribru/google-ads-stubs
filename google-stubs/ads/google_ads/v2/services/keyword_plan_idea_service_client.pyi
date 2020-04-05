import grpc  # type: ignore
from google.ads.google_ads.v2.services.transports.keyword_plan_idea_service_grpc_transport import (
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

from google.protobuf.wrappers_pb2 import StringValue

from google.ads.google_ads.v2.proto.services.keyword_plan_idea_service_pb2 import (
    KeywordAndUrlSeed,
    KeywordSeed,
    GenerateKeywordIdeaResponse,
)

from typing_extensions import TypedDict

from google.ads.google_ads.v2.proto.enums.keyword_plan_network_pb2 import (
    KeywordPlanNetworkEnum,
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
        keyword_seed: Optional[Any] = ...,
        url_seed: Optional[Union[Dict[str, Any], KeywordSeed]] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> GenerateKeywordIdeaResponse: ...
