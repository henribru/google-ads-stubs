from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask

from google.ads.googleads.v10.resources.types.campaign_conversion_goal import (
    CampaignConversionGoal,
)

class CampaignConversionGoalOperation(proto.Message):
    update_mask: FieldMask
    update: CampaignConversionGoal
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        update: CampaignConversionGoal = ...
    ) -> None: ...

class MutateCampaignConversionGoalResult(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...

class MutateCampaignConversionGoalsRequest(proto.Message):
    customer_id: str
    operations: list[CampaignConversionGoalOperation]
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[CampaignConversionGoalOperation] = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateCampaignConversionGoalsResponse(proto.Message):
    results: list[MutateCampaignConversionGoalResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: list[MutateCampaignConversionGoalResult] = ...
    ) -> None: ...
