from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask

from google.ads.googleads.v13.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v13.resources.types.custom_conversion_goal import (
    CustomConversionGoal,
)

_M = TypeVar("_M")

class CustomConversionGoalOperation(proto.Message):
    update_mask: FieldMask
    create: CustomConversionGoal
    update: CustomConversionGoal
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        create: CustomConversionGoal = ...,
        update: CustomConversionGoal = ...,
        remove: str = ...
    ) -> None: ...

class MutateCustomConversionGoalResult(proto.Message):
    resource_name: str
    custom_conversion_goal: CustomConversionGoal
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        custom_conversion_goal: CustomConversionGoal = ...
    ) -> None: ...

class MutateCustomConversionGoalsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[CustomConversionGoalOperation]
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[CustomConversionGoalOperation] = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateCustomConversionGoalsResponse(proto.Message):
    results: MutableSequence[MutateCustomConversionGoalResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        results: MutableSequence[MutateCustomConversionGoalResult] = ...
    ) -> None: ...
