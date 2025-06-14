from google.ads.googleads.v18.resources.types.campaign_lifecycle_goal import CampaignLifecycleGoal
from google.ads.googleads.v18.resources.types.campaign_lifecycle_goal import CampaignLifecycleGoal
from google.protobuf.field_mask_pb2 import FieldMask
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class CampaignLifecycleGoalOperation(proto.Message):
    update_mask: FieldMask
    create: CampaignLifecycleGoal
    update: CampaignLifecycleGoal
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, update_mask: FieldMask = ..., create: CampaignLifecycleGoal = ..., update: CampaignLifecycleGoal = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["update_mask", "create", "update"]) -> bool: ...
class ConfigureCampaignLifecycleGoalsRequest(proto.Message):
    customer_id: str
    operation: CampaignLifecycleGoalOperation
    validate_only: bool
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, customer_id: str = ..., operation: CampaignLifecycleGoalOperation = ..., validate_only: bool = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "operation", "validate_only"]) -> bool: ...
class ConfigureCampaignLifecycleGoalsResponse(proto.Message):
    result: ConfigureCampaignLifecycleGoalsResult
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, result: ConfigureCampaignLifecycleGoalsResult = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["result"]) -> bool: ...
class ConfigureCampaignLifecycleGoalsResult(proto.Message):
    resource_name: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name"]) -> bool: ...
