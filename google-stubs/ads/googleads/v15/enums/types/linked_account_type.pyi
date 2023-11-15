from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class LinkedAccountTypeEnum(proto.Message):
    class LinkedAccountType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        THIRD_PARTY_APP_ANALYTICS = 2
        DATA_PARTNER = 3
        GOOGLE_ADS = 4
        ADVERTISING_PARTNER = 6
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
