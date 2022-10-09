import abc
from typing import Awaitable, Callable, Optional, Sequence, Union

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v11.services.types import reach_plan_service

class ReachPlanServiceTransport(abc.ABC):
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
    def list_plannable_locations(
        self,
    ) -> Callable[
        [reach_plan_service.ListPlannableLocationsRequest],
        Union[
            reach_plan_service.ListPlannableLocationsResponse,
            Awaitable[reach_plan_service.ListPlannableLocationsResponse],
        ],
    ]: ...
    @property
    def list_plannable_products(
        self,
    ) -> Callable[
        [reach_plan_service.ListPlannableProductsRequest],
        Union[
            reach_plan_service.ListPlannableProductsResponse,
            Awaitable[reach_plan_service.ListPlannableProductsResponse],
        ],
    ]: ...
    @property
    def generate_product_mix_ideas(
        self,
    ) -> Callable[
        [reach_plan_service.GenerateProductMixIdeasRequest],
        Union[
            reach_plan_service.GenerateProductMixIdeasResponse,
            Awaitable[reach_plan_service.GenerateProductMixIdeasResponse],
        ],
    ]: ...
    @property
    def generate_reach_forecast(
        self,
    ) -> Callable[
        [reach_plan_service.GenerateReachForecastRequest],
        Union[
            reach_plan_service.GenerateReachForecastResponse,
            Awaitable[reach_plan_service.GenerateReachForecastResponse],
        ],
    ]: ...
