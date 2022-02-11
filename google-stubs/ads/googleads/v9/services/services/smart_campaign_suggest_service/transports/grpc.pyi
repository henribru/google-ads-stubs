from typing import Callable, Optional, Sequence, Tuple

import grpc
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v9.services.types import smart_campaign_suggest_service

from .base import SmartCampaignSuggestServiceTransport

class SmartCampaignSuggestServiceGrpcTransport(SmartCampaignSuggestServiceTransport):
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        credentials_file: str = ...,
        scopes: Sequence[str] = ...,
        channel: grpc.Channel = ...,
        api_mtls_endpoint: str = ...,
        client_cert_source: Callable[[], Tuple[bytes, bytes]] = ...,
        ssl_channel_credentials: grpc.ChannelCredentials = ...,
        quota_project_id: Optional[str] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @classmethod
    def create_channel(
        cls,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        scopes: Optional[Sequence[str]] = ...,
        **kwargs
    ) -> grpc.Channel: ...
    def close(self) -> None: ...
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
