from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v14.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v14.resources.types.conversion_value_rule import (
    ConversionValueRule,
)

_M = TypeVar("_M")

class ConversionValueRuleOperation(proto.Message):
    update_mask: FieldMask
    create: ConversionValueRule
    update: ConversionValueRule
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        create: ConversionValueRule = ...,
        update: ConversionValueRule = ...,
        remove: str = ...
    ) -> None: ...

class MutateConversionValueRuleResult(proto.Message):
    resource_name: str
    conversion_value_rule: ConversionValueRule
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        conversion_value_rule: ConversionValueRule = ...
    ) -> None: ...

class MutateConversionValueRulesRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[ConversionValueRuleOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[ConversionValueRuleOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateConversionValueRulesResponse(proto.Message):
    results: MutableSequence[MutateConversionValueRuleResult]
    partial_failure_error: Status
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        results: MutableSequence[MutateConversionValueRuleResult] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...
