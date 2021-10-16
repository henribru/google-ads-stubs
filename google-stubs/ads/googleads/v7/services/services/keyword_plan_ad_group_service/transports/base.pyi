import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import keyword_plan_ad_group
from google.ads.googleads.v7.services.types import keyword_plan_ad_group_service

class KeywordPlanAdGroupServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_keyword_plan_ad_group(
        self,
    ) -> typing.Callable[
        [keyword_plan_ad_group_service.GetKeywordPlanAdGroupRequest],
        keyword_plan_ad_group.KeywordPlanAdGroup,
    ]: ...
    @property
    def mutate_keyword_plan_ad_groups(
        self,
    ) -> typing.Callable[
        [keyword_plan_ad_group_service.MutateKeywordPlanAdGroupsRequest],
        keyword_plan_ad_group_service.MutateKeywordPlanAdGroupsResponse,
    ]: ...
