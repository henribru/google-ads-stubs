from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class PolicyReviewStatusEnum(proto.Message):
    class PolicyReviewStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        REVIEW_IN_PROGRESS = 2
        REVIEWED = 3
        UNDER_APPEAL = 4
        ELIGIBLE_MAY_SERVE = 5
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
