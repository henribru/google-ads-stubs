from google.ads.google_ads.v3.proto.services import (
    product_bidding_category_constant_service_pb2 as product_bidding_category_constant_service_pb2,
)
from google.ads.google_ads.v3.services import (
    product_bidding_category_constant_service_client_config as product_bidding_category_constant_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    product_bidding_category_constant_service_grpc_transport as product_bidding_category_constant_service_grpc_transport,
)
from google.oauth2 import service_account as service_account  # type: ignore
import grpc  # type: ignore
from google.ads.google_ads.v3.services.transports.product_bidding_category_constant_service_grpc_transport import (
    ProductBiddingCategoryConstantServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v3.proto.resources.product_bidding_category_constant_pb2 import (
    ProductBiddingCategoryConstant,
)

class ProductBiddingCategoryConstantServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> ProductBiddingCategoryConstantServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> ProductBiddingCategoryConstantServiceClient: ...
    @classmethod
    def product_bidding_category_constant_path(
        cls, product_bidding_category_constant: Any
    ): ...
    transport: Union[
        ProductBiddingCategoryConstantServiceGrpcTransport,
        Callable[
            [Credentials, type], ProductBiddingCategoryConstantServiceGrpcTransport
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                ProductBiddingCategoryConstantServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    ProductBiddingCategoryConstantServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_product_bidding_category_constant(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> ProductBiddingCategoryConstant: ...
