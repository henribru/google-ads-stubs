from typing import Any

import proto

__protobuf__: Any

class FunctionErrorEnum(proto.Message):
    class FunctionError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        INVALID_FUNCTION_FORMAT: int
        DATA_TYPE_MISMATCH: int
        INVALID_CONJUNCTION_OPERANDS: int
        INVALID_NUMBER_OF_OPERANDS: int
        INVALID_OPERAND_TYPE: int
        INVALID_OPERATOR: int
        INVALID_REQUEST_CONTEXT_TYPE: int
        INVALID_FUNCTION_FOR_CALL_PLACEHOLDER: int
        INVALID_FUNCTION_FOR_PLACEHOLDER: int
        INVALID_OPERAND: int
        MISSING_CONSTANT_OPERAND_VALUE: int
        INVALID_CONSTANT_OPERAND_VALUE: int
        INVALID_NESTING: int
        MULTIPLE_FEED_IDS_NOT_SUPPORTED: int
        INVALID_FUNCTION_FOR_FEED_WITH_FIXED_SCHEMA: int
        INVALID_ATTRIBUTE_NAME: int
