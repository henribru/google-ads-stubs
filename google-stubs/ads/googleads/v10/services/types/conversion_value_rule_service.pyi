from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v10.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v10.resources.types.conversion_value_rule import (
    ConversionValueRule,
)

class ConversionValueRuleOperation(proto.Message):
    update_mask: FieldMask
    create: ConversionValueRule
    update: ConversionValueRule
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: ConversionValueRule = ...,
        update: ConversionValueRule = ...,
        remove: str = ...
    ) -> None: ...

class MutateConversionValueRuleResult(proto.Message):
    resource_name: str
    conversion_value_rule: ConversionValueRule
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        conversion_value_rule: ConversionValueRule = ...
    ) -> None: ...

class MutateConversionValueRulesRequest(proto.Message):
    customer_id: str
    operations: list[ConversionValueRuleOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[ConversionValueRuleOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateConversionValueRulesResponse(proto.Message):
    results: list[MutateConversionValueRuleResult]
    partial_failure_error: Status
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: list[MutateConversionValueRuleResult] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...
