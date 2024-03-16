import abc
from typing import Awaitable, Callable, Sequence

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v14.services.types import reach_plan_service

__all__ = ["ReachPlanServiceTransport"]

class ReachPlanServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(
        self,
        *,
        host: str = "googleads.googleapis.com",
        credentials: ga_credentials.Credentials | None = None,
        credentials_file: str | None = None,
        scopes: Sequence[str] | None = None,
        quota_project_id: str | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: bool | None = False,
        **kwargs,
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def list_plannable_locations(
        self,
    ) -> Callable[
        [reach_plan_service.ListPlannableLocationsRequest],
        reach_plan_service.ListPlannableLocationsResponse
        | Awaitable[reach_plan_service.ListPlannableLocationsResponse],
    ]: ...
    @property
    def list_plannable_products(
        self,
    ) -> Callable[
        [reach_plan_service.ListPlannableProductsRequest],
        reach_plan_service.ListPlannableProductsResponse
        | Awaitable[reach_plan_service.ListPlannableProductsResponse],
    ]: ...
    @property
    def generate_reach_forecast(
        self,
    ) -> Callable[
        [reach_plan_service.GenerateReachForecastRequest],
        reach_plan_service.GenerateReachForecastResponse
        | Awaitable[reach_plan_service.GenerateReachForecastResponse],
    ]: ...
