from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class ManagerLinkStatusEnum(proto.Message):
    class ManagerLinkStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ACTIVE = 2
        INACTIVE = 3
        PENDING = 4
        REFUSED = 5
        CANCELED = 6

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
