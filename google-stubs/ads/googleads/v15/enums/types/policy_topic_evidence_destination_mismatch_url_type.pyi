from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class PolicyTopicEvidenceDestinationMismatchUrlTypeEnum(proto.Message):
    class PolicyTopicEvidenceDestinationMismatchUrlType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DISPLAY_URL = 2
        FINAL_URL = 3
        FINAL_MOBILE_URL = 4
        TRACKING_URL = 5
        MOBILE_TRACKING_URL = 6
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
