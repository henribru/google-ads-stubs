from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status
from typing_extensions import Literal

from google.ads.googleads.v13.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v13.resources.types.conversion_value_rule_set import (
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
    def __contains__(self, key: Literal["update_mask", "create", "update", "remove"]) -> bool: ...  # type: ignore[override]

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
    def __contains__(self, key: Literal["resource_name", "conversion_value_rule_set"]) -> bool: ...  # type: ignore[override]

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
    def __contains__(self, key: Literal["customer_id", "operations", "partial_failure", "validate_only", "response_content_type"]) -> bool: ...  # type: ignore[override]

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
    def __contains__(self, key: Literal["results", "partial_failure_error"]) -> bool: ...  # type: ignore[override]
