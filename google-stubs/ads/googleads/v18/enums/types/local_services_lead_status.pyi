from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class LocalServicesLeadStatusEnum(proto.Message):
    class LeadStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NEW = 2
        ACTIVE = 3
        BOOKED = 4
        DECLINED = 5
        EXPIRED = 6
        DISABLED = 7
        CONSUMER_DECLINED = 8
        WIPED_OUT = 9

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
