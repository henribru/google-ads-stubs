from typing import Any

import proto

from google.ads.googleads.v11.enums.types.matching_function_context_type import (
    MatchingFunctionContextTypeEnum,
)
from google.ads.googleads.v11.enums.types.matching_function_operator import (
    MatchingFunctionOperatorEnum,
)

class MatchingFunction(proto.Message):
    function_string: str
    operator: MatchingFunctionOperatorEnum.MatchingFunctionOperator
    left_operands: list[Operand]
    right_operands: list[Operand]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        function_string: str = ...,
        operator: MatchingFunctionOperatorEnum.MatchingFunctionOperator = ...,
        left_operands: list[Operand] = ...,
        right_operands: list[Operand] = ...
    ) -> None: ...

class Operand(proto.Message):
    class ConstantOperand(proto.Message):
        string_value: str
        long_value: int
        boolean_value: bool
        double_value: float
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            string_value: str = ...,
            long_value: int = ...,
            boolean_value: bool = ...,
            double_value: float = ...
        ) -> None: ...

    class FeedAttributeOperand(proto.Message):
        feed_id: int
        feed_attribute_id: int
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            feed_id: int = ...,
            feed_attribute_id: int = ...
        ) -> None: ...

    class FunctionOperand(proto.Message):
        matching_function: MatchingFunction
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            matching_function: MatchingFunction = ...
        ) -> None: ...

    class RequestContextOperand(proto.Message):
        context_type: MatchingFunctionContextTypeEnum.MatchingFunctionContextType
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            context_type: MatchingFunctionContextTypeEnum.MatchingFunctionContextType = ...
        ) -> None: ...
    constant_operand: Operand.ConstantOperand
    feed_attribute_operand: Operand.FeedAttributeOperand
    function_operand: Operand.FunctionOperand
    request_context_operand: Operand.RequestContextOperand
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        constant_operand: Operand.ConstantOperand = ...,
        feed_attribute_operand: Operand.FeedAttributeOperand = ...,
        function_operand: Operand.FunctionOperand = ...,
        request_context_operand: Operand.RequestContextOperand = ...
    ) -> None: ...
