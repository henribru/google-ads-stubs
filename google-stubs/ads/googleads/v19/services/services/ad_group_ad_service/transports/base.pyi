import abc
from _typeshed import Incomplete
from google.ads.googleads.v19.services.types import ad_group_ad_service
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials
from google.protobuf import empty_pb2
from typing import Awaitable, Callable, Sequence

__all__ = ['AdGroupAdServiceTransport']

class AdGroupAdServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(self, *, host: str = ..., credentials: ga_credentials.Credentials | None = None, credentials_file: str | None = None, scopes: Sequence[str] | None = None, quota_project_id: str | None = None, client_info: gapic_v1.client_info.ClientInfo = ..., always_use_jwt_access: bool | None = False, api_audience: str | None = None, **kwargs) -> None: ...
    @property
    def host(self): ...
    def close(self) -> None: ...
    @property
    def mutate_ad_group_ads(self) -> Callable[[ad_group_ad_service.MutateAdGroupAdsRequest], ad_group_ad_service.MutateAdGroupAdsResponse | Awaitable[ad_group_ad_service.MutateAdGroupAdsResponse]]: ...
    @property
    def remove_automatically_created_assets(self) -> Callable[[ad_group_ad_service.RemoveAutomaticallyCreatedAssetsRequest], empty_pb2.Empty | Awaitable[empty_pb2.Empty]]: ...
    @property
    def kind(self) -> str: ...
