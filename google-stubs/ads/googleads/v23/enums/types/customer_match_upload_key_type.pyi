from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class CustomerMatchUploadKeyTypeEnum(proto.Message):
    class CustomerMatchUploadKeyType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CONTACT_INFO = 2
        CRM_ID = 3
        MOBILE_ADVERTISING_ID = 4

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
