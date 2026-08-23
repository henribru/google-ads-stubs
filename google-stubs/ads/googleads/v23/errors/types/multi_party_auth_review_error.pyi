from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class MultiPartyAuthReviewErrorEnum(proto.Message):
    class MultiPartyAuthReviewError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ACCESS_INVITATION_NOT_FOUND = 2
        ACCESS_INVITATION_INVALID_STATUS = 3
        INVALID_STATUS_TRANSITION = 4
        PERMISSION_DENIED = 5

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
