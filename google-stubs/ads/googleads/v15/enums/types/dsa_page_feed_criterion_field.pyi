from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class DsaPageFeedCriterionFieldEnum(proto.Message):
    class DsaPageFeedCriterionField(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        PAGE_URL = 2
        LABEL = 3
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
