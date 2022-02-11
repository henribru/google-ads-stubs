import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v9.services.types import reach_plan_service

class ReachPlanServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def list_plannable_locations(
        self,
    ) -> typing.Callable[
        [reach_plan_service.ListPlannableLocationsRequest],
        reach_plan_service.ListPlannableLocationsResponse,
    ]: ...
    @property
    def list_plannable_products(
        self,
    ) -> typing.Callable[
        [reach_plan_service.ListPlannableProductsRequest],
        reach_plan_service.ListPlannableProductsResponse,
    ]: ...
    @property
    def generate_product_mix_ideas(
        self,
    ) -> typing.Callable[
        [reach_plan_service.GenerateProductMixIdeasRequest],
        reach_plan_service.GenerateProductMixIdeasResponse,
    ]: ...
    @property
    def generate_reach_forecast(
        self,
    ) -> typing.Callable[
        [reach_plan_service.GenerateReachForecastRequest],
        reach_plan_service.GenerateReachForecastResponse,
    ]: ...
