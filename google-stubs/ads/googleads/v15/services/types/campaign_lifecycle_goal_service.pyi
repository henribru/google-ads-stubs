from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask

from google.ads.googleads.v15.resources.types.campaign_lifecycle_goal import (
    CampaignLifecycleGoal,
)

class CampaignLifecycleGoalOperation(proto.Message):
    update_mask: FieldMask
    create: CampaignLifecycleGoal
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: CampaignLifecycleGoal = ...
    ) -> None: ...

class ConfigureCampaignLifecycleGoalsRequest(proto.Message):
    customer_id: str
    operation: CampaignLifecycleGoalOperation
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operation: CampaignLifecycleGoalOperation = ...,
        validate_only: bool = ...
    ) -> None: ...

class ConfigureCampaignLifecycleGoalsResponse(proto.Message):
    result: ConfigureCampaignLifecycleGoalsResult
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        result: ConfigureCampaignLifecycleGoalsResult = ...
    ) -> None: ...

class ConfigureCampaignLifecycleGoalsResult(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...