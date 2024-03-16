from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class CustomerFeedErrorEnum(proto.Message):
    class CustomerFeedError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE = 2
        CANNOT_CREATE_FOR_REMOVED_FEED = 3
        CANNOT_CREATE_ALREADY_EXISTING_CUSTOMER_FEED = 4
        CANNOT_MODIFY_REMOVED_CUSTOMER_FEED = 5
        INVALID_PLACEHOLDER_TYPE = 6
        MISSING_FEEDMAPPING_FOR_PLACEHOLDER_TYPE = 7
        PLACEHOLDER_TYPE_NOT_ALLOWED_ON_CUSTOMER_FEED = 8

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
