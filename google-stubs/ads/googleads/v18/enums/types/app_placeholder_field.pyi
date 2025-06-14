import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class AppPlaceholderFieldEnum(proto.Message):
    class AppPlaceholderField(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        STORE = 2
        ID = 3
        LINK_TEXT = 4
        URL = 5
        FINAL_URLS = 6
        FINAL_MOBILE_URLS = 7
        TRACKING_URL = 8
        FINAL_URL_SUFFIX = 9
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
