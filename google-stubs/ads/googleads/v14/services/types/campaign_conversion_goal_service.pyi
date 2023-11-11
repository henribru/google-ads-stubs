from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask

from google.ads.googleads.v14.resources.types.campaign_conversion_goal import (
    CampaignConversionGoal,
)

_M = TypeVar("_M")

class CampaignConversionGoalOperation(proto.Message):
    update_mask: FieldMask
    update: CampaignConversionGoal
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        update: CampaignConversionGoal = ...
    ) -> None: ...

class MutateCampaignConversionGoalResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...

class MutateCampaignConversionGoalsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[CampaignConversionGoalOperation]
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: MutableSequence[CampaignConversionGoalOperation] = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateCampaignConversionGoalsResponse(proto.Message):
    results: MutableSequence[MutateCampaignConversionGoalResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: MutableSequence[MutateCampaignConversionGoalResult] = ...
    ) -> None: ...
