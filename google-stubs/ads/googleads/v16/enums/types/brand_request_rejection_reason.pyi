from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class BrandRequestRejectionReasonEnum(proto.Message):
    class BrandRequestRejectionReason(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        EXISTING_BRAND = 2
        EXISTING_BRAND_VARIANT = 3
        INCORRECT_INFORMATION = 4
        NOT_A_BRAND = 5

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
