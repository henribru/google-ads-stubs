import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class BrandRequestRejectionReasonEnum(proto.Message):
    class BrandRequestRejectionReason(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        EXISTING_BRAND = 2
        EXISTING_BRAND_VARIANT = 3
        INCORRECT_INFORMATION = 4
        NOT_A_BRAND = 5
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
