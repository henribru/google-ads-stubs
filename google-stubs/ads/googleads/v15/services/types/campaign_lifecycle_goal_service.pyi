from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from typing_extensions import Literal

from google.ads.googleads.v15.resources.types.campaign_lifecycle_goal import (
    CampaignLifecycleGoal,
)

_M = TypeVar("_M")

class CampaignLifecycleGoalOperation(proto.Message):
    update_mask: FieldMask
    create: CampaignLifecycleGoal
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        create: CampaignLifecycleGoal = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["update_mask", "create"]
    ) -> bool: ...

class ConfigureCampaignLifecycleGoalsRequest(proto.Message):
    customer_id: str
    operation: CampaignLifecycleGoalOperation
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operation: CampaignLifecycleGoalOperation = ...,
        validate_only: bool = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["customer_id", "operation", "validate_only"]
    ) -> bool: ...

class ConfigureCampaignLifecycleGoalsResponse(proto.Message):
    result: ConfigureCampaignLifecycleGoalsResult
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        result: ConfigureCampaignLifecycleGoalsResult = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["result"]
    ) -> bool: ...

class ConfigureCampaignLifecycleGoalsResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["resource_name"]
    ) -> bool: ...
