from typing import Callable, Optional, Sequence, Tuple

import grpc
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v13.services.types import smart_campaign_suggest_service

from .base import SmartCampaignSuggestServiceTransport

class SmartCampaignSuggestServiceGrpcTransport(SmartCampaignSuggestServiceTransport):
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: Optional[ga_credentials.Credentials] = ...,
        credentials_file: Optional[str] = ...,
        scopes: Optional[Sequence[str]] = ...,
        channel: Optional[grpc.Channel] = ...,
        api_mtls_endpoint: Optional[str] = ...,
        client_cert_source: Optional[Callable[[], Tuple[bytes, bytes]]] = ...,
        ssl_channel_credentials: Optional[grpc.ChannelCredentials] = ...,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = ...,
        quota_project_id: Optional[str] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: Optional[bool] = ...
    ) -> None: ...
    @classmethod
    def create_channel(
        cls,
        host: str = ...,
        credentials: Optional[ga_credentials.Credentials] = ...,
        credentials_file: Optional[str] = ...,
        scopes: Optional[Sequence[str]] = ...,
        quota_project_id: Optional[str] = ...,
        **kwargs
    ) -> grpc.Channel: ...
    @property
    def grpc_channel(self) -> grpc.Channel: ...
    @property
    def suggest_smart_campaign_budget_options(
        self,
    ) -> Callable[
        [smart_campaign_suggest_service.SuggestSmartCampaignBudgetOptionsRequest],
        smart_campaign_suggest_service.SuggestSmartCampaignBudgetOptionsResponse,
    ]: ...
    @property
    def suggest_smart_campaign_ad(
        self,
    ) -> Callable[
        [smart_campaign_suggest_service.SuggestSmartCampaignAdRequest],
        smart_campaign_suggest_service.SuggestSmartCampaignAdResponse,
    ]: ...
    @property
    def suggest_keyword_themes(
        self,
    ) -> Callable[
        [smart_campaign_suggest_service.SuggestKeywordThemesRequest],
        smart_campaign_suggest_service.SuggestKeywordThemesResponse,
    ]: ...
    def close(self) -> None: ...
