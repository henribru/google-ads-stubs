import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import recommendation
from google.ads.googleads.v8.services.types import recommendation_service

class RecommendationServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_recommendation(
        self,
    ) -> typing.Callable[
        [recommendation_service.GetRecommendationRequest], recommendation.Recommendation
    ]: ...
    @property
    def apply_recommendation(
        self,
    ) -> typing.Callable[
        [recommendation_service.ApplyRecommendationRequest],
        recommendation_service.ApplyRecommendationResponse,
    ]: ...
    @property
    def dismiss_recommendation(
        self,
    ) -> typing.Callable[
        [recommendation_service.DismissRecommendationRequest],
        recommendation_service.DismissRecommendationResponse,
    ]: ...
