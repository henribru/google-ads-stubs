from google.ads.googleads.v18.enums.types.matching_function_context_type import MatchingFunctionContextTypeEnum
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from google.ads.googleads.v18.enums.types.matching_function_operator import MatchingFunctionOperatorEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class MatchingFunction(proto.Message):
    function_string: str
    operator: MatchingFunctionOperatorEnum.MatchingFunctionOperator
    left_operands: MutableSequence[Operand]
    right_operands: MutableSequence[Operand]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., function_string: str = ..., operator: MatchingFunctionOperatorEnum.MatchingFunctionOperator = ..., left_operands: MutableSequence[Operand] = ..., right_operands: MutableSequence[Operand] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["function_string", "operator", "left_operands", "right_operands"]) -> bool: ...
class Operand(proto.Message):
    class ConstantOperand(proto.Message):
        string_value: str
        long_value: int
        boolean_value: bool
        double_value: float
        def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., string_value: str = ..., long_value: int = ..., boolean_value: bool = ..., double_value: float = ...) -> None: ...
        def __contains__(  # type: ignore[override]
        self, key: Literal["string_value", "long_value", "boolean_value", "double_value"]) -> bool: ...
    class FeedAttributeOperand(proto.Message):
        feed_id: int
        feed_attribute_id: int
        def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., feed_id: int = ..., feed_attribute_id: int = ...) -> None: ...
        def __contains__(  # type: ignore[override]
        self, key: Literal["feed_id", "feed_attribute_id"]) -> bool: ...
    class FunctionOperand(proto.Message):
        matching_function: MatchingFunction
        def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., matching_function: MatchingFunction = ...) -> None: ...
        def __contains__(  # type: ignore[override]
        self, key: Literal["matching_function"]) -> bool: ...
    class RequestContextOperand(proto.Message):
        context_type: MatchingFunctionContextTypeEnum.MatchingFunctionContextType
        def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., context_type: MatchingFunctionContextTypeEnum.MatchingFunctionContextType = ...) -> None: ...
        def __contains__(  # type: ignore[override]
        self, key: Literal["context_type"]) -> bool: ...
    constant_operand: Operand.ConstantOperand
    feed_attribute_operand: Operand.FeedAttributeOperand
    function_operand: Operand.FunctionOperand
    request_context_operand: Operand.RequestContextOperand
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., constant_operand: Operand.ConstantOperand = ..., feed_attribute_operand: Operand.FeedAttributeOperand = ..., function_operand: Operand.FunctionOperand = ..., request_context_operand: Operand.RequestContextOperand = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["constant_operand", "feed_attribute_operand", "function_operand", "request_context_operand"]) -> bool: ...
