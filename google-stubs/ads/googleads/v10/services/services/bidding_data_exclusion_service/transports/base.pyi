import abc
from typing import Awaitable, Callable, Optional, Sequence, Union

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v10.services.types import bidding_data_exclusion_service

class BiddingDataExclusionServiceTransport(abc.ABC):
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
    def mutate_bidding_data_exclusions(
        self,
    ) -> Callable[
        [bidding_data_exclusion_service.MutateBiddingDataExclusionsRequest],
        Union[
            bidding_data_exclusion_service.MutateBiddingDataExclusionsResponse,
            Awaitable[
                bidding_data_exclusion_service.MutateBiddingDataExclusionsResponse
            ],
        ],
    ]: ...
