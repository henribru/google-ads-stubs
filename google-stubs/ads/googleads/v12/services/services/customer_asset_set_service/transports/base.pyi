import abc
from typing import Awaitable, Callable, Optional, Sequence, Union

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v12.services.types import customer_asset_set_service

class CustomerAssetSetServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        credentials_file: Optional[str] = ...,
        scopes: Optional[Sequence[str]] = ...,
        quota_project_id: Optional[str] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: Optional[bool] = ...,
        **kwargs
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def mutate_customer_asset_sets(
        self,
    ) -> Callable[
        [customer_asset_set_service.MutateCustomerAssetSetsRequest],
        Union[
            customer_asset_set_service.MutateCustomerAssetSetsResponse,
            Awaitable[customer_asset_set_service.MutateCustomerAssetSetsResponse],
        ],
    ]: ...
