from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class LocalServicesVerificationArtifactTypeEnum(proto.Message):
    class LocalServicesVerificationArtifactType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        BACKGROUND_CHECK = 2
        INSURANCE = 3
        LICENSE = 4
        BUSINESS_REGISTRATION_CHECK = 5

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
