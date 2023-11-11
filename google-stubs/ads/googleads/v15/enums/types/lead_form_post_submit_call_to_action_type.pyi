from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class LeadFormPostSubmitCallToActionTypeEnum(proto.Message):
    class LeadFormPostSubmitCallToActionType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        VISIT_SITE = 2
        DOWNLOAD = 3
        LEARN_MORE = 4
        SHOP_NOW = 5
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
