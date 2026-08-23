from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class LoyaltyMembershipEnum(proto.Message):
    class LoyaltyMembership(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NONMEMBER = 2
        TIER1 = 3
        TIER2 = 4
        TIER3 = 5
        TIER4 = 6
        TIER5 = 7
        TIER6 = 8
        TIER7 = 9

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
