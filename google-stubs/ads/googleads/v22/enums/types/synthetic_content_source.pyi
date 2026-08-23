from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class SyntheticContentSourceEnum(proto.Message):
    class SyntheticContentSource(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ADVERTISER_ATTESTED = 2
        GOOGLE_GENERATED_ADVERTISER_REVIEWED = 3
        GOOGLE_GENERATED_FULLY_AUTOMATED = 4

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
