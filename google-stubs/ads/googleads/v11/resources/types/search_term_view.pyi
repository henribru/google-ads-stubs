from typing import Any

import proto

from google.ads.googleads.v11.enums.types.search_term_targeting_status import (
    SearchTermTargetingStatusEnum,
)

class SearchTermView(proto.Message):
    resource_name: str
    search_term: str
    ad_group: str
    status: SearchTermTargetingStatusEnum.SearchTermTargetingStatus
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        search_term: str = ...,
        ad_group: str = ...,
        status: SearchTermTargetingStatusEnum.SearchTermTargetingStatus = ...
    ) -> None: ...
