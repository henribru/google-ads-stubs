from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class FeedMappingCriterionTypeEnum(proto.Message):
    class FeedMappingCriterionType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        LOCATION_EXTENSION_TARGETING = 4
        DSA_PAGE_FEED = 3
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
