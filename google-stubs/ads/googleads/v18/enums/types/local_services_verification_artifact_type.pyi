import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class LocalServicesVerificationArtifactTypeEnum(proto.Message):
    class LocalServicesVerificationArtifactType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        BACKGROUND_CHECK = 2
        INSURANCE = 3
        LICENSE = 4
        BUSINESS_REGISTRATION_CHECK = 5
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
