from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class BrandGuidelinesMigrationErrorEnum(proto.Message):
    class BrandGuidelinesMigrationError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        BRAND_GUIDELINES_ALREADY_ENABLED = 2
        CANNOT_ENABLE_BRAND_GUIDELINES_FOR_REMOVED_CAMPAIGN = 3
        BRAND_GUIDELINES_LOGO_LIMIT_EXCEEDED = 4
        CANNOT_AUTO_POPULATE_BRAND_ASSETS_WHEN_BRAND_ASSETS_PROVIDED = 5
        AUTO_POPULATE_BRAND_ASSETS_REQUIRED_WHEN_BRAND_ASSETS_OMITTED = 6
        TOO_MANY_ENABLE_OPERATIONS = 7

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
