from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v23.common.types.goal_common import (
    CustomerLifecycleOptimizationValueSettings,
)
from google.ads.googleads.v23.enums.types.customer_lifecycle_optimization_mode import (
    CustomerLifecycleOptimizationModeEnum,
)

_M = TypeVar("_M")

class CampaignGoalSettings(proto.Message):
    class CampaignRetentionGoalSettings(proto.Message):
        value_settings_override: CustomerLifecycleOptimizationValueSettings
        target_option: (
            CustomerLifecycleOptimizationModeEnum.CustomerLifecycleOptimizationMode
        )
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            value_settings_override: CustomerLifecycleOptimizationValueSettings = ...,
            target_option: CustomerLifecycleOptimizationModeEnum.CustomerLifecycleOptimizationMode = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["value_settings_override", "target_option"]
        ) -> bool: ...

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
