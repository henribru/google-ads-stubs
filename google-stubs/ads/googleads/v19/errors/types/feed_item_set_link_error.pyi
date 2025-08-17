from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class FeedItemSetLinkErrorEnum(proto.Message):
    class FeedItemSetLinkError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        FEED_ID_MISMATCH = 2
        NO_MUTATE_ALLOWED_FOR_DYNAMIC_SET = 3

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
