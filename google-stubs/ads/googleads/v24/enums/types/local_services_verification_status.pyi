from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class LocalServicesVerificationStatusEnum(proto.Message):
    class LocalServicesVerificationStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NEEDS_REVIEW = 2
        FAILED = 3
        PASSED = 4
        NOT_APPLICABLE = 5
        NO_SUBMISSION = 6
        PARTIAL_SUBMISSION = 7
        PENDING_ESCALATION = 8

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
