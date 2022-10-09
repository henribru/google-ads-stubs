import proto
from _typeshed import Incomplete

from google.ads.googleads.v11.enums.types import (
    matching_function_context_type as matching_function_context_type,
    matching_function_operator as matching_function_operator,
)

__protobuf__: Incomplete

class MatchingFunction(proto.Message):
    function_string: Incomplete
    operator: Incomplete
    left_operands: Incomplete
    right_operands: Incomplete

class Operand(proto.Message):
    class ConstantOperand(proto.Message):
        string_value: Incomplete
        long_value: Incomplete
        boolean_value: Incomplete
        double_value: Incomplete

    class FeedAttributeOperand(proto.Message):
        feed_id: Incomplete
        feed_attribute_id: Incomplete

    class FunctionOperand(proto.Message):
        matching_function: Incomplete

    class RequestContextOperand(proto.Message):
        context_type: Incomplete
    constant_operand: Incomplete
    feed_attribute_operand: Incomplete
    function_operand: Incomplete
    request_context_operand: Incomplete
