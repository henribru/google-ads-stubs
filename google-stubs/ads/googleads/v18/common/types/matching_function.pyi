import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import matching_function_context_type, matching_function_operator
from typing import MutableSequence

__protobuf__: Incomplete

class MatchingFunction(proto.Message):
    function_string: str
    operator: matching_function_operator.MatchingFunctionOperatorEnum.MatchingFunctionOperator
    left_operands: MutableSequence['Operand']
    right_operands: MutableSequence['Operand']

class Operand(proto.Message):
    class ConstantOperand(proto.Message):
        string_value: str
        long_value: int
        boolean_value: bool
        double_value: float
    class FeedAttributeOperand(proto.Message):
        feed_id: int
        feed_attribute_id: int
    class FunctionOperand(proto.Message):
        matching_function: MatchingFunction
    class RequestContextOperand(proto.Message):
        context_type: matching_function_context_type.MatchingFunctionContextTypeEnum.MatchingFunctionContextType
    constant_operand: ConstantOperand
    feed_attribute_operand: FeedAttributeOperand
    function_operand: FunctionOperand
    request_context_operand: RequestContextOperand
