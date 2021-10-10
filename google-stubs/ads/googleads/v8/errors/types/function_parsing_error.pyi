from typing import Any

import proto

__protobuf__: Any

class FunctionParsingErrorEnum(proto.Message):
    class FunctionParsingError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        NO_MORE_INPUT: int
        EXPECTED_CHARACTER: int
        UNEXPECTED_SEPARATOR: int
        UNMATCHED_LEFT_BRACKET: int
        UNMATCHED_RIGHT_BRACKET: int
        TOO_MANY_NESTED_FUNCTIONS: int
        MISSING_RIGHT_HAND_OPERAND: int
        INVALID_OPERATOR_NAME: int
        FEED_ATTRIBUTE_OPERAND_ARGUMENT_NOT_INTEGER: int
        NO_OPERANDS: int
        TOO_MANY_OPERANDS: int
