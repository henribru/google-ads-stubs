from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from typing_extensions import Literal

from google.ads.googleads.v14.resources.types.campaign_conversion_goal import (
    CampaignConversionGoal,
)

_M = TypeVar("_M")

class CampaignConversionGoalOperation(proto.Message):
    update_mask: FieldMask
    update: CampaignConversionGoal
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        update: CampaignConversionGoal = ...
    ) -> None: ...
    def __contains__(self, key: Literal["update_mask", "update"]) -> bool: ...  # type: ignore[override]

class MutateCampaignConversionGoalResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name"]) -> bool: ...  # type: ignore[override]

class MutateCampaignConversionGoalsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[CampaignConversionGoalOperation]
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[CampaignConversionGoalOperation] = ...,
        validate_only: bool = ...
    ) -> None: ...
    def __contains__(self, key: Literal["customer_id", "operations", "validate_only"]) -> bool: ...  # type: ignore[override]

class MutateCampaignConversionGoalsResponse(proto.Message):
    results: MutableSequence[MutateCampaignConversionGoalResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        results: MutableSequence[MutateCampaignConversionGoalResult] = ...
    ) -> None: ...
    def __contains__(self, key: Literal["results"]) -> bool: ...  # type: ignore[override]
