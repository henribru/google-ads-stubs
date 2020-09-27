# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import NewType as typing___NewType, cast as typing___cast

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)
from google.protobuf.message import Message as google___protobuf___message___Message

builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class QueryErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    QueryErrorValue = typing___NewType("QueryErrorValue", builtin___int)
    type___QueryErrorValue = QueryErrorValue
    QueryError: _QueryError
    class _QueryError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            QueryErrorEnum.QueryErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(QueryErrorEnum.QueryErrorValue, 0)
        UNKNOWN = typing___cast(QueryErrorEnum.QueryErrorValue, 1)
        QUERY_ERROR = typing___cast(QueryErrorEnum.QueryErrorValue, 50)
        BAD_ENUM_CONSTANT = typing___cast(QueryErrorEnum.QueryErrorValue, 18)
        BAD_ESCAPE_SEQUENCE = typing___cast(QueryErrorEnum.QueryErrorValue, 7)
        BAD_FIELD_NAME = typing___cast(QueryErrorEnum.QueryErrorValue, 12)
        BAD_LIMIT_VALUE = typing___cast(QueryErrorEnum.QueryErrorValue, 15)
        BAD_NUMBER = typing___cast(QueryErrorEnum.QueryErrorValue, 5)
        BAD_OPERATOR = typing___cast(QueryErrorEnum.QueryErrorValue, 3)
        BAD_PARAMETER_NAME = typing___cast(QueryErrorEnum.QueryErrorValue, 61)
        BAD_PARAMETER_VALUE = typing___cast(QueryErrorEnum.QueryErrorValue, 62)
        BAD_RESOURCE_TYPE_IN_FROM_CLAUSE = typing___cast(
            QueryErrorEnum.QueryErrorValue, 45
        )
        BAD_SYMBOL = typing___cast(QueryErrorEnum.QueryErrorValue, 2)
        BAD_VALUE = typing___cast(QueryErrorEnum.QueryErrorValue, 4)
        DATE_RANGE_TOO_WIDE = typing___cast(QueryErrorEnum.QueryErrorValue, 36)
        DATE_RANGE_TOO_NARROW = typing___cast(QueryErrorEnum.QueryErrorValue, 60)
        EXPECTED_AND = typing___cast(QueryErrorEnum.QueryErrorValue, 30)
        EXPECTED_BY = typing___cast(QueryErrorEnum.QueryErrorValue, 14)
        EXPECTED_DIMENSION_FIELD_IN_SELECT_CLAUSE = typing___cast(
            QueryErrorEnum.QueryErrorValue, 37
        )
        EXPECTED_FILTERS_ON_DATE_RANGE = typing___cast(
            QueryErrorEnum.QueryErrorValue, 55
        )
        EXPECTED_FROM = typing___cast(QueryErrorEnum.QueryErrorValue, 44)
        EXPECTED_LIST = typing___cast(QueryErrorEnum.QueryErrorValue, 41)
        EXPECTED_REFERENCED_FIELD_IN_SELECT_CLAUSE = typing___cast(
            QueryErrorEnum.QueryErrorValue, 16
        )
        EXPECTED_SELECT = typing___cast(QueryErrorEnum.QueryErrorValue, 13)
        EXPECTED_SINGLE_VALUE = typing___cast(QueryErrorEnum.QueryErrorValue, 42)
        EXPECTED_VALUE_WITH_BETWEEN_OPERATOR = typing___cast(
            QueryErrorEnum.QueryErrorValue, 29
        )
        INVALID_DATE_FORMAT = typing___cast(QueryErrorEnum.QueryErrorValue, 38)
        INVALID_STRING_VALUE = typing___cast(QueryErrorEnum.QueryErrorValue, 57)
        INVALID_VALUE_WITH_BETWEEN_OPERATOR = typing___cast(
            QueryErrorEnum.QueryErrorValue, 26
        )
        INVALID_VALUE_WITH_DURING_OPERATOR = typing___cast(
            QueryErrorEnum.QueryErrorValue, 22
        )
        INVALID_VALUE_WITH_LIKE_OPERATOR = typing___cast(
            QueryErrorEnum.QueryErrorValue, 56
        )
        OPERATOR_FIELD_MISMATCH = typing___cast(QueryErrorEnum.QueryErrorValue, 35)
        PROHIBITED_EMPTY_LIST_IN_CONDITION = typing___cast(
            QueryErrorEnum.QueryErrorValue, 28
        )
        PROHIBITED_ENUM_CONSTANT = typing___cast(QueryErrorEnum.QueryErrorValue, 54)
        PROHIBITED_FIELD_COMBINATION_IN_SELECT_CLAUSE = typing___cast(
            QueryErrorEnum.QueryErrorValue, 31
        )
        PROHIBITED_FIELD_IN_ORDER_BY_CLAUSE = typing___cast(
            QueryErrorEnum.QueryErrorValue, 40
        )
        PROHIBITED_FIELD_IN_SELECT_CLAUSE = typing___cast(
            QueryErrorEnum.QueryErrorValue, 23
        )
        PROHIBITED_FIELD_IN_WHERE_CLAUSE = typing___cast(
            QueryErrorEnum.QueryErrorValue, 24
        )
        PROHIBITED_RESOURCE_TYPE_IN_FROM_CLAUSE = typing___cast(
            QueryErrorEnum.QueryErrorValue, 43
        )
        PROHIBITED_RESOURCE_TYPE_IN_SELECT_CLAUSE = typing___cast(
            QueryErrorEnum.QueryErrorValue, 48
        )
        PROHIBITED_RESOURCE_TYPE_IN_WHERE_CLAUSE = typing___cast(
            QueryErrorEnum.QueryErrorValue, 58
        )
        PROHIBITED_METRIC_IN_SELECT_OR_WHERE_CLAUSE = typing___cast(
            QueryErrorEnum.QueryErrorValue, 49
        )
        PROHIBITED_SEGMENT_IN_SELECT_OR_WHERE_CLAUSE = typing___cast(
            QueryErrorEnum.QueryErrorValue, 51
        )
        PROHIBITED_SEGMENT_WITH_METRIC_IN_SELECT_OR_WHERE_CLAUSE = typing___cast(
            QueryErrorEnum.QueryErrorValue, 53
        )
        LIMIT_VALUE_TOO_LOW = typing___cast(QueryErrorEnum.QueryErrorValue, 25)
        PROHIBITED_NEWLINE_IN_STRING = typing___cast(QueryErrorEnum.QueryErrorValue, 8)
        PROHIBITED_VALUE_COMBINATION_IN_LIST = typing___cast(
            QueryErrorEnum.QueryErrorValue, 10
        )
        PROHIBITED_VALUE_COMBINATION_WITH_BETWEEN_OPERATOR = typing___cast(
            QueryErrorEnum.QueryErrorValue, 21
        )
        STRING_NOT_TERMINATED = typing___cast(QueryErrorEnum.QueryErrorValue, 6)
        TOO_MANY_SEGMENTS = typing___cast(QueryErrorEnum.QueryErrorValue, 34)
        UNEXPECTED_END_OF_QUERY = typing___cast(QueryErrorEnum.QueryErrorValue, 9)
        UNEXPECTED_FROM_CLAUSE = typing___cast(QueryErrorEnum.QueryErrorValue, 47)
        UNRECOGNIZED_FIELD = typing___cast(QueryErrorEnum.QueryErrorValue, 32)
        UNEXPECTED_INPUT = typing___cast(QueryErrorEnum.QueryErrorValue, 11)
        REQUESTED_METRICS_FOR_MANAGER = typing___cast(
            QueryErrorEnum.QueryErrorValue, 59
        )
    UNSPECIFIED = typing___cast(QueryErrorEnum.QueryErrorValue, 0)
    UNKNOWN = typing___cast(QueryErrorEnum.QueryErrorValue, 1)
    QUERY_ERROR = typing___cast(QueryErrorEnum.QueryErrorValue, 50)
    BAD_ENUM_CONSTANT = typing___cast(QueryErrorEnum.QueryErrorValue, 18)
    BAD_ESCAPE_SEQUENCE = typing___cast(QueryErrorEnum.QueryErrorValue, 7)
    BAD_FIELD_NAME = typing___cast(QueryErrorEnum.QueryErrorValue, 12)
    BAD_LIMIT_VALUE = typing___cast(QueryErrorEnum.QueryErrorValue, 15)
    BAD_NUMBER = typing___cast(QueryErrorEnum.QueryErrorValue, 5)
    BAD_OPERATOR = typing___cast(QueryErrorEnum.QueryErrorValue, 3)
    BAD_PARAMETER_NAME = typing___cast(QueryErrorEnum.QueryErrorValue, 61)
    BAD_PARAMETER_VALUE = typing___cast(QueryErrorEnum.QueryErrorValue, 62)
    BAD_RESOURCE_TYPE_IN_FROM_CLAUSE = typing___cast(QueryErrorEnum.QueryErrorValue, 45)
    BAD_SYMBOL = typing___cast(QueryErrorEnum.QueryErrorValue, 2)
    BAD_VALUE = typing___cast(QueryErrorEnum.QueryErrorValue, 4)
    DATE_RANGE_TOO_WIDE = typing___cast(QueryErrorEnum.QueryErrorValue, 36)
    DATE_RANGE_TOO_NARROW = typing___cast(QueryErrorEnum.QueryErrorValue, 60)
    EXPECTED_AND = typing___cast(QueryErrorEnum.QueryErrorValue, 30)
    EXPECTED_BY = typing___cast(QueryErrorEnum.QueryErrorValue, 14)
    EXPECTED_DIMENSION_FIELD_IN_SELECT_CLAUSE = typing___cast(
        QueryErrorEnum.QueryErrorValue, 37
    )
    EXPECTED_FILTERS_ON_DATE_RANGE = typing___cast(QueryErrorEnum.QueryErrorValue, 55)
    EXPECTED_FROM = typing___cast(QueryErrorEnum.QueryErrorValue, 44)
    EXPECTED_LIST = typing___cast(QueryErrorEnum.QueryErrorValue, 41)
    EXPECTED_REFERENCED_FIELD_IN_SELECT_CLAUSE = typing___cast(
        QueryErrorEnum.QueryErrorValue, 16
    )
    EXPECTED_SELECT = typing___cast(QueryErrorEnum.QueryErrorValue, 13)
    EXPECTED_SINGLE_VALUE = typing___cast(QueryErrorEnum.QueryErrorValue, 42)
    EXPECTED_VALUE_WITH_BETWEEN_OPERATOR = typing___cast(
        QueryErrorEnum.QueryErrorValue, 29
    )
    INVALID_DATE_FORMAT = typing___cast(QueryErrorEnum.QueryErrorValue, 38)
    INVALID_STRING_VALUE = typing___cast(QueryErrorEnum.QueryErrorValue, 57)
    INVALID_VALUE_WITH_BETWEEN_OPERATOR = typing___cast(
        QueryErrorEnum.QueryErrorValue, 26
    )
    INVALID_VALUE_WITH_DURING_OPERATOR = typing___cast(
        QueryErrorEnum.QueryErrorValue, 22
    )
    INVALID_VALUE_WITH_LIKE_OPERATOR = typing___cast(QueryErrorEnum.QueryErrorValue, 56)
    OPERATOR_FIELD_MISMATCH = typing___cast(QueryErrorEnum.QueryErrorValue, 35)
    PROHIBITED_EMPTY_LIST_IN_CONDITION = typing___cast(
        QueryErrorEnum.QueryErrorValue, 28
    )
    PROHIBITED_ENUM_CONSTANT = typing___cast(QueryErrorEnum.QueryErrorValue, 54)
    PROHIBITED_FIELD_COMBINATION_IN_SELECT_CLAUSE = typing___cast(
        QueryErrorEnum.QueryErrorValue, 31
    )
    PROHIBITED_FIELD_IN_ORDER_BY_CLAUSE = typing___cast(
        QueryErrorEnum.QueryErrorValue, 40
    )
    PROHIBITED_FIELD_IN_SELECT_CLAUSE = typing___cast(
        QueryErrorEnum.QueryErrorValue, 23
    )
    PROHIBITED_FIELD_IN_WHERE_CLAUSE = typing___cast(QueryErrorEnum.QueryErrorValue, 24)
    PROHIBITED_RESOURCE_TYPE_IN_FROM_CLAUSE = typing___cast(
        QueryErrorEnum.QueryErrorValue, 43
    )
    PROHIBITED_RESOURCE_TYPE_IN_SELECT_CLAUSE = typing___cast(
        QueryErrorEnum.QueryErrorValue, 48
    )
    PROHIBITED_RESOURCE_TYPE_IN_WHERE_CLAUSE = typing___cast(
        QueryErrorEnum.QueryErrorValue, 58
    )
    PROHIBITED_METRIC_IN_SELECT_OR_WHERE_CLAUSE = typing___cast(
        QueryErrorEnum.QueryErrorValue, 49
    )
    PROHIBITED_SEGMENT_IN_SELECT_OR_WHERE_CLAUSE = typing___cast(
        QueryErrorEnum.QueryErrorValue, 51
    )
    PROHIBITED_SEGMENT_WITH_METRIC_IN_SELECT_OR_WHERE_CLAUSE = typing___cast(
        QueryErrorEnum.QueryErrorValue, 53
    )
    LIMIT_VALUE_TOO_LOW = typing___cast(QueryErrorEnum.QueryErrorValue, 25)
    PROHIBITED_NEWLINE_IN_STRING = typing___cast(QueryErrorEnum.QueryErrorValue, 8)
    PROHIBITED_VALUE_COMBINATION_IN_LIST = typing___cast(
        QueryErrorEnum.QueryErrorValue, 10
    )
    PROHIBITED_VALUE_COMBINATION_WITH_BETWEEN_OPERATOR = typing___cast(
        QueryErrorEnum.QueryErrorValue, 21
    )
    STRING_NOT_TERMINATED = typing___cast(QueryErrorEnum.QueryErrorValue, 6)
    TOO_MANY_SEGMENTS = typing___cast(QueryErrorEnum.QueryErrorValue, 34)
    UNEXPECTED_END_OF_QUERY = typing___cast(QueryErrorEnum.QueryErrorValue, 9)
    UNEXPECTED_FROM_CLAUSE = typing___cast(QueryErrorEnum.QueryErrorValue, 47)
    UNRECOGNIZED_FIELD = typing___cast(QueryErrorEnum.QueryErrorValue, 32)
    UNEXPECTED_INPUT = typing___cast(QueryErrorEnum.QueryErrorValue, 11)
    REQUESTED_METRICS_FOR_MANAGER = typing___cast(QueryErrorEnum.QueryErrorValue, 59)
    type___QueryError = QueryError
    def __init__(self,) -> None: ...

type___QueryErrorEnum = QueryErrorEnum