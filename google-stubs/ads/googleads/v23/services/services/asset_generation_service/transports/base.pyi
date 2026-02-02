import abc
from _typeshed import Incomplete
from google.ads.googleads.v23.services.types import asset_generation_service
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials
from typing import Awaitable, Callable, Sequence

__all__ = ['AssetGenerationServiceTransport']

class AssetGenerationServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(self, *, host: str = 'googleads.googleapis.com', credentials: ga_credentials.Credentials | None = None, credentials_file: str | None = None, scopes: Sequence[str] | None = None, quota_project_id: str | None = None, client_info: gapic_v1.client_info.ClientInfo = ..., always_use_jwt_access: bool | None = False, api_audience: str | None = None, **kwargs) -> None: ...
    @property
    def host(self): ...
    def close(self) -> None: ...
    @property
    def generate_text(self) -> Callable[[asset_generation_service.GenerateTextRequest], asset_generation_service.GenerateTextResponse | Awaitable[asset_generation_service.GenerateTextResponse]]: ...
    @property
    def generate_images(self) -> Callable[[asset_generation_service.GenerateImagesRequest], asset_generation_service.GenerateImagesResponse | Awaitable[asset_generation_service.GenerateImagesResponse]]: ...
    @property
    def kind(self) -> str: ...
