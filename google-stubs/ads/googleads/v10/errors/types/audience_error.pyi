from typing import Any

import proto

class AudienceErrorEnum(proto.Message):
    class AudienceError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NAME_ALREADY_IN_USE = 2
        DIMENSION_INVALID = 3
        AUDIENCE_SEGMENT_NOT_FOUND = 4
        AUDIENCE_SEGMENT_TYPE_NOT_SUPPORTED = 5
        DUPLICATE_AUDIENCE_SEGMENT = 6
        TOO_MANY_SEGMENTS = 7
        TOO_MANY_DIMENSIONS_OF_SAME_TYPE = 8
        IN_USE = 9
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
