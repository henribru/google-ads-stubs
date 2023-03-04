from typing import Any

import proto

class FunctionParsingErrorEnum(proto.Message):
    class FunctionParsingError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NO_MORE_INPUT = 2
        EXPECTED_CHARACTER = 3
        UNEXPECTED_SEPARATOR = 4
        UNMATCHED_LEFT_BRACKET = 5
        UNMATCHED_RIGHT_BRACKET = 6
        TOO_MANY_NESTED_FUNCTIONS = 7
        MISSING_RIGHT_HAND_OPERAND = 8
        INVALID_OPERATOR_NAME = 9
        FEED_ATTRIBUTE_OPERAND_ARGUMENT_NOT_INTEGER = 10
        NO_OPERANDS = 11
        TOO_MANY_OPERANDS = 12
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
