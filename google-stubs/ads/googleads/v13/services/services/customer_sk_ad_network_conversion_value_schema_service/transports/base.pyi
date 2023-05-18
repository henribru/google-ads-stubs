import abc
from typing import Awaitable, Callable, Optional, Sequence, Union

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v13.services.types import (
    customer_sk_ad_network_conversion_value_schema_service,
)

class CustomerSkAdNetworkConversionValueSchemaServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: Optional[ga_credentials.Credentials] = ...,
        credentials_file: Optional[str] = ...,
        scopes: Optional[Sequence[str]] = ...,
        quota_project_id: Optional[str] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: Optional[bool] = ...,
        **kwargs
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def mutate_customer_sk_ad_network_conversion_value_schema(
        self,
    ) -> Callable[
        [
            customer_sk_ad_network_conversion_value_schema_service.MutateCustomerSkAdNetworkConversionValueSchemaRequest
        ],
        Union[
            customer_sk_ad_network_conversion_value_schema_service.MutateCustomerSkAdNetworkConversionValueSchemaResponse,
            Awaitable[
                customer_sk_ad_network_conversion_value_schema_service.MutateCustomerSkAdNetworkConversionValueSchemaResponse
            ],
        ],
    ]: ...
