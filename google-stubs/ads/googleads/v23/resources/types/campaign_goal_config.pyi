from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v23.common.types.campaign_goal_settings import (
    CampaignGoalSettings,
)
from google.ads.googleads.v23.enums.types.goal_type import GoalTypeEnum

_M = TypeVar("_M")

class CampaignGoalConfig(proto.Message):
    resource_name: str
    campaign: str
    goal: str
    goal_type: GoalTypeEnum.GoalType
    campaign_retention_settings: CampaignGoalSettings.CampaignRetentionGoalSettings
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        campaign: str = ...,
        goal: str = ...,
        goal_type: GoalTypeEnum.GoalType = ...,
        campaign_retention_settings: CampaignGoalSettings.CampaignRetentionGoalSettings = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "campaign",
            "goal",
            "goal_type",
            "campaign_retention_settings",
        ],
    ) -> bool: ...
