from typing import Any

import proto

class ConversionEnvironmentEnum(proto.Message):
    class ConversionEnvironment(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        APP = 2
        WEB = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
