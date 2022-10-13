from typing import Any

import proto

class FunctionErrorEnum(proto.Message):
    class FunctionError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_FUNCTION_FORMAT = 2
        DATA_TYPE_MISMATCH = 3
        INVALID_CONJUNCTION_OPERANDS = 4
        INVALID_NUMBER_OF_OPERANDS = 5
        INVALID_OPERAND_TYPE = 6
        INVALID_OPERATOR = 7
        INVALID_REQUEST_CONTEXT_TYPE = 8
        INVALID_FUNCTION_FOR_CALL_PLACEHOLDER = 9
        INVALID_FUNCTION_FOR_PLACEHOLDER = 10
        INVALID_OPERAND = 11
        MISSING_CONSTANT_OPERAND_VALUE = 12
        INVALID_CONSTANT_OPERAND_VALUE = 13
        INVALID_NESTING = 14
        MULTIPLE_FEED_IDS_NOT_SUPPORTED = 15
        INVALID_FUNCTION_FOR_FEED_WITH_FIXED_SCHEMA = 16
        INVALID_ATTRIBUTE_NAME = 17
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
