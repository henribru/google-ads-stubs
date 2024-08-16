from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class CallPlaceholderFieldEnum(proto.Message):
    class CallPlaceholderField(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        PHONE_NUMBER = 2
        COUNTRY_CODE = 3
        TRACKED = 4
        CONVERSION_TYPE_ID = 5
        CONVERSION_REPORTING_STATE = 6

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
