import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class CustomerMatchUploadKeyTypeEnum(proto.Message):
    class CustomerMatchUploadKeyType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CONTACT_INFO = 2
        CRM_ID = 3
        MOBILE_ADVERTISING_ID = 4
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
