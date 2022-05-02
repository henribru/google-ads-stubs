import abc
from typing import Awaitable, Callable, Optional, Sequence, Union

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v10.services.types import (
    bidding_seasonality_adjustment_service,
)

class BiddingSeasonalityAdjustmentServiceTransport(abc.ABC):
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
    def mutate_bidding_seasonality_adjustments(
        self,
    ) -> Callable[
        [
            bidding_seasonality_adjustment_service.MutateBiddingSeasonalityAdjustmentsRequest
        ],
        Union[
            bidding_seasonality_adjustment_service.MutateBiddingSeasonalityAdjustmentsResponse,
            Awaitable[
                bidding_seasonality_adjustment_service.MutateBiddingSeasonalityAdjustmentsResponse
            ],
        ],
    ]: ...
