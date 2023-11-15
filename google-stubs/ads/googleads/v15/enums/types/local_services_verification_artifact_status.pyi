from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class LocalServicesVerificationArtifactStatusEnum(proto.Message):
    class LocalServicesVerificationArtifactStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        PASSED = 2
        FAILED = 3
        PENDING = 4
        NO_SUBMISSION = 5
        CANCELLED = 6
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
