from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class IdentityVerificationProgramStatusEnum(proto.Message):
    class IdentityVerificationProgramStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        PENDING_USER_ACTION = 2
        PENDING_REVIEW = 3
        SUCCESS = 4
        FAILURE = 5

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
