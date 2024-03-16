from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class SmartCampaignErrorEnum(proto.Message):
    class SmartCampaignError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_BUSINESS_LOCATION_ID = 2
        INVALID_CAMPAIGN = 3
        BUSINESS_NAME_OR_BUSINESS_LOCATION_ID_MISSING = 4
        REQUIRED_SUGGESTION_FIELD_MISSING = 5
        GEO_TARGETS_REQUIRED = 6
        CANNOT_DETERMINE_SUGGESTION_LOCALE = 7
        FINAL_URL_NOT_CRAWLABLE = 8

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
