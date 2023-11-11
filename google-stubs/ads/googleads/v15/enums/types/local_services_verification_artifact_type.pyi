from typing import Any

import proto

class LocalServicesVerificationArtifactTypeEnum(proto.Message):
    class LocalServicesVerificationArtifactType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        BACKGROUND_CHECK = 2
        INSURANCE = 3
        LICENSE = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
