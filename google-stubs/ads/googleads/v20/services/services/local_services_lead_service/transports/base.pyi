import abc
from typing import Awaitable, Callable, Sequence

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v20.services.types import local_services_lead_service

__all__ = ["LocalServicesLeadServiceTransport"]

class LocalServicesLeadServiceTransport(abc.ABC):
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
        api_audience: str | None = None,
        **kwargs,
    ) -> None: ...
    @property
    def host(self): ...
    def close(self) -> None: ...
    @property
    def append_lead_conversation(
        self,
    ) -> Callable[
        [local_services_lead_service.AppendLeadConversationRequest],
        local_services_lead_service.AppendLeadConversationResponse
        | Awaitable[local_services_lead_service.AppendLeadConversationResponse],
    ]: ...
    @property
    def provide_lead_feedback(
        self,
    ) -> Callable[
        [local_services_lead_service.ProvideLeadFeedbackRequest],
        local_services_lead_service.ProvideLeadFeedbackResponse
        | Awaitable[local_services_lead_service.ProvideLeadFeedbackResponse],
    ]: ...
    @property
    def kind(self) -> str: ...
