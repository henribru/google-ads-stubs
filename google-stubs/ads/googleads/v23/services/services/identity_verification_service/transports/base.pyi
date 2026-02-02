import abc
from _typeshed import Incomplete
from google.ads.googleads.v23.services.types import identity_verification_service
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials
from google.protobuf import empty_pb2
from typing import Awaitable, Callable, Sequence

__all__ = ['IdentityVerificationServiceTransport']

class IdentityVerificationServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(self, *, host: str = 'googleads.googleapis.com', credentials: ga_credentials.Credentials | None = None, credentials_file: str | None = None, scopes: Sequence[str] | None = None, quota_project_id: str | None = None, client_info: gapic_v1.client_info.ClientInfo = ..., always_use_jwt_access: bool | None = False, api_audience: str | None = None, **kwargs) -> None: ...
    @property
    def host(self): ...
    def close(self) -> None: ...
    @property
    def start_identity_verification(self) -> Callable[[identity_verification_service.StartIdentityVerificationRequest], empty_pb2.Empty | Awaitable[empty_pb2.Empty]]: ...
    @property
    def get_identity_verification(self) -> Callable[[identity_verification_service.GetIdentityVerificationRequest], identity_verification_service.GetIdentityVerificationResponse | Awaitable[identity_verification_service.GetIdentityVerificationResponse]]: ...
    @property
    def kind(self) -> str: ...
