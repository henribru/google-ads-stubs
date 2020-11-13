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

from google.ads.google_ads.v6.proto.services import (
    google_ads_service_pb2 as google_ads_service_pb2,
)
from google.ads.google_ads.v6.services import (
    google_ads_service_client_config as google_ads_service_client_config,
)
from google.ads.google_ads.v6.services.transports import (
    google_ads_service_grpc_transport as google_ads_service_grpc_transport,
)
from google.ads.google_ads.v6.types import (
    GoogleAdsRow,
    MutateGoogleAdsResponse,
    MutateOperation,
    ResponseContentTypeEnum,
    SearchGoogleAdsStreamResponse,
    SummaryRowSettingEnum,
)

class GoogleAdsServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> GoogleAdsServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> GoogleAdsServiceClient: ...
    transport: Union[
        google_ads_service_grpc_transport.GoogleAdsServiceGrpcTransport,
        Callable[
            [Credentials, type],
            google_ads_service_grpc_transport.GoogleAdsServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                google_ads_service_grpc_transport.GoogleAdsServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    google_ads_service_grpc_transport.GoogleAdsServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
        client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    ) -> None: ...
    def search(
        self,
        customer_id: str,
        query: str,
        page_size: Optional[int] = ...,
        validate_only: Optional[bool] = ...,
        return_total_results_count: Optional[bool] = ...,
        summary_row_setting: Optional[
            SummaryRowSettingEnum.SummaryRowSettingValue
        ] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> Iterable[GoogleAdsRow]: ...
    def search_stream(
        self,
        customer_id: str,
        query: str,
        summary_row_setting: Optional[
            SummaryRowSettingEnum.SummaryRowSettingValue
        ] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> Iterable[SearchGoogleAdsStreamResponse]: ...
    def mutate(
        self,
        customer_id: str,
        mutate_operations: List[Union[Dict[str, Any], MutateOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        response_content_type: Optional[
            ResponseContentTypeEnum.ResponseContentTypeValue
        ] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateGoogleAdsResponse: ...
