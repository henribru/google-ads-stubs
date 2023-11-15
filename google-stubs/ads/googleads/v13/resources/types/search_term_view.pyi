from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v13.enums.types.search_term_targeting_status import (
    SearchTermTargetingStatusEnum,
)

_M = TypeVar("_M")

class SearchTermView(proto.Message):
    resource_name: str
    search_term: str
    ad_group: str
    status: SearchTermTargetingStatusEnum.SearchTermTargetingStatus
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        search_term: str = ...,
        ad_group: str = ...,
        status: SearchTermTargetingStatusEnum.SearchTermTargetingStatus = ...
    ) -> None: ...
