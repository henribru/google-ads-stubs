from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class LocationExtensionTargetingCriterionFieldEnum(proto.Message):
    class LocationExtensionTargetingCriterionField(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ADDRESS_LINE_1 = 2
        ADDRESS_LINE_2 = 3
        CITY = 4
        PROVINCE = 5
        POSTAL_CODE = 6
        COUNTRY_CODE = 7
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
