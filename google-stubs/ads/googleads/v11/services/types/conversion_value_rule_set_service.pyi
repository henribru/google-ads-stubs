from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v11.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v11.resources.types.conversion_value_rule_set import (
    ConversionValueRuleSet,
)

class ConversionValueRuleSetOperation(proto.Message):
    update_mask: FieldMask
    create: ConversionValueRuleSet
    update: ConversionValueRuleSet
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: ConversionValueRuleSet = ...,
        update: ConversionValueRuleSet = ...,
        remove: str = ...
    ) -> None: ...

class MutateConversionValueRuleSetResult(proto.Message):
    resource_name: str
    conversion_value_rule_set: ConversionValueRuleSet
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        conversion_value_rule_set: ConversionValueRuleSet = ...
    ) -> None: ...

class MutateConversionValueRuleSetsRequest(proto.Message):
    customer_id: str
    operations: list[ConversionValueRuleSetOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[ConversionValueRuleSetOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateConversionValueRuleSetsResponse(proto.Message):
    results: list[MutateConversionValueRuleSetResult]
    partial_failure_error: Status
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: list[MutateConversionValueRuleSetResult] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...
