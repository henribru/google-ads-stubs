from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class AdGroupCriterionApprovalStatusEnum(proto.Message):
    class AdGroupCriterionApprovalStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        APPROVED = 2
        DISAPPROVED = 3
        PENDING_REVIEW = 4
        UNDER_REVIEW = 5
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
