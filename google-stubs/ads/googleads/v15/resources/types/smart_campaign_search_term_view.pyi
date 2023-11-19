from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class SmartCampaignSearchTermView(proto.Message):
    resource_name: str
    search_term: str
    campaign: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        search_term: str = ...,
        campaign: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name", "search_term", "campaign"]) -> bool: ...  # type: ignore[override]
