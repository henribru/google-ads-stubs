from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class DataLinkStatusEnum(proto.Message):
    class DataLinkStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        REQUESTED = 2
        PENDING_APPROVAL = 3
        ENABLED = 4
        DISABLED = 5
        REVOKED = 6
        REJECTED = 7

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
