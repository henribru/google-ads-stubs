import abc
from typing import Awaitable, Callable, Sequence

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v15.services.types import recommendation_service

__all__ = ["RecommendationServiceTransport"]

class RecommendationServiceTransport(abc.ABC):
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
    def apply_recommendation(
        self,
    ) -> Callable[
        [recommendation_service.ApplyRecommendationRequest],
        recommendation_service.ApplyRecommendationResponse
        | Awaitable[recommendation_service.ApplyRecommendationResponse],
    ]: ...
    @property
    def dismiss_recommendation(
        self,
    ) -> Callable[
        [recommendation_service.DismissRecommendationRequest],
        recommendation_service.DismissRecommendationResponse
        | Awaitable[recommendation_service.DismissRecommendationResponse],
    ]: ...
