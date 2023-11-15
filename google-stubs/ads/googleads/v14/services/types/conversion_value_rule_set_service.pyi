from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v14.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v14.resources.types.conversion_value_rule_set import (
    ConversionValueRuleSet,
)

_M = TypeVar("_M")

class ConversionValueRuleSetOperation(proto.Message):
    update_mask: FieldMask
    create: ConversionValueRuleSet
    update: ConversionValueRuleSet
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        create: ConversionValueRuleSet = ...,
        update: ConversionValueRuleSet = ...,
        remove: str = ...
    ) -> None: ...

class MutateConversionValueRuleSetResult(proto.Message):
    resource_name: str
    conversion_value_rule_set: ConversionValueRuleSet
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        conversion_value_rule_set: ConversionValueRuleSet = ...
    ) -> None: ...

class MutateConversionValueRuleSetsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[ConversionValueRuleSetOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[ConversionValueRuleSetOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateConversionValueRuleSetsResponse(proto.Message):
    results: MutableSequence[MutateConversionValueRuleSetResult]
    partial_failure_error: Status
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        results: MutableSequence[MutateConversionValueRuleSetResult] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...
