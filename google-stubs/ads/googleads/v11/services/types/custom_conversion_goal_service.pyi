from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask

from google.ads.googleads.v11.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v11.resources.types.custom_conversion_goal import (
    CustomConversionGoal,
)

class CustomConversionGoalOperation(proto.Message):
    update_mask: FieldMask
    create: CustomConversionGoal
    update: CustomConversionGoal
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: CustomConversionGoal = ...,
        update: CustomConversionGoal = ...,
        remove: str = ...
    ) -> None: ...

class MutateCustomConversionGoalResult(proto.Message):
    resource_name: str
    custom_conversion_goal: CustomConversionGoal
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        custom_conversion_goal: CustomConversionGoal = ...
    ) -> None: ...

class MutateCustomConversionGoalsRequest(proto.Message):
    customer_id: str
    operations: list[CustomConversionGoalOperation]
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[CustomConversionGoalOperation] = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateCustomConversionGoalsResponse(proto.Message):
    results: list[MutateCustomConversionGoalResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: list[MutateCustomConversionGoalResult] = ...
    ) -> None: ...
