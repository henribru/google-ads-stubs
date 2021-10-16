from typing import Callable, Optional, Sequence, Tuple

import grpc
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import keyword_plan_ad_group_keyword
from google.ads.googleads.v8.services.types import keyword_plan_ad_group_keyword_service

from .base import KeywordPlanAdGroupKeywordServiceTransport

class KeywordPlanAdGroupKeywordServiceGrpcTransport(
    KeywordPlanAdGroupKeywordServiceTransport
):
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
    @property
    def grpc_channel(self) -> grpc.Channel: ...
    @property
    def get_keyword_plan_ad_group_keyword(
        self,
    ) -> Callable[
        [keyword_plan_ad_group_keyword_service.GetKeywordPlanAdGroupKeywordRequest],
        keyword_plan_ad_group_keyword.KeywordPlanAdGroupKeyword,
    ]: ...
    @property
    def mutate_keyword_plan_ad_group_keywords(
        self,
    ) -> Callable[
        [keyword_plan_ad_group_keyword_service.MutateKeywordPlanAdGroupKeywordsRequest],
        keyword_plan_ad_group_keyword_service.MutateKeywordPlanAdGroupKeywordsResponse,
    ]: ...
