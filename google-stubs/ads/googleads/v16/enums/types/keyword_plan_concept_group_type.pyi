from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class KeywordPlanConceptGroupTypeEnum(proto.Message):
    class KeywordPlanConceptGroupType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        BRAND = 2
        OTHER_BRANDS = 3
        NON_BRAND = 4

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
