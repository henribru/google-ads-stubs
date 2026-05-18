from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class IdentityVerificationErrorEnum(proto.Message):
    class IdentityVerificationError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NO_EFFECTIVE_BILLING = 2
        BILLING_NOT_ON_MONTHLY_INVOICING = 3
        VERIFICATION_ALREADY_STARTED = 4

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
