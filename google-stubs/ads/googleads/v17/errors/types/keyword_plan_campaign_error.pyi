from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class KeywordPlanCampaignErrorEnum(proto.Message):
    class KeywordPlanCampaignError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_NAME = 2
        INVALID_LANGUAGES = 3
        INVALID_GEOS = 4
        DUPLICATE_NAME = 5
        MAX_GEOS_EXCEEDED = 6
        MAX_LANGUAGES_EXCEEDED = 7

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
