from typing import Any

import proto

from google.ads.googleads.v8.enums.types import (
    matching_function_context_type as matching_function_context_type,
    matching_function_operator as matching_function_operator,
)

__protobuf__: Any

class MatchingFunction(proto.Message):
    function_string: Any
    operator: Any
    left_operands: Any
    right_operands: Any

class Operand(proto.Message):
    class ConstantOperand(proto.Message):
        string_value: Any
        long_value: Any
        boolean_value: Any
        double_value: Any
    class FeedAttributeOperand(proto.Message):
        feed_id: Any
        feed_attribute_id: Any
    class FunctionOperand(proto.Message):
        matching_function: Any
    class RequestContextOperand(proto.Message):
        context_type: Any
    constant_operand: Any
    feed_attribute_operand: Any
    function_operand: Any
    request_context_operand: Any
