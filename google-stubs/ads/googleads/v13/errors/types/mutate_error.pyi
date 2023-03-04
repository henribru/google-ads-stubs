from typing import Any

import proto

class MutateErrorEnum(proto.Message):
    class MutateError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        RESOURCE_NOT_FOUND = 3
        ID_EXISTS_IN_MULTIPLE_MUTATES = 7
        INCONSISTENT_FIELD_VALUES = 8
        MUTATE_NOT_ALLOWED = 9
        RESOURCE_NOT_IN_GOOGLE_ADS = 10
        RESOURCE_ALREADY_EXISTS = 11
        RESOURCE_DOES_NOT_SUPPORT_VALIDATE_ONLY = 12
        OPERATION_DOES_NOT_SUPPORT_PARTIAL_FAILURE = 16
        RESOURCE_READ_ONLY = 13
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
