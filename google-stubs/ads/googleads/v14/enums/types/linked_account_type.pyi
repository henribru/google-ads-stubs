from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class LinkedAccountTypeEnum(proto.Message):
    class LinkedAccountType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        THIRD_PARTY_APP_ANALYTICS = 2
        DATA_PARTNER = 3
        GOOGLE_ADS = 4
        HOTEL_CENTER = 5
        ADVERTISING_PARTNER = 6

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
