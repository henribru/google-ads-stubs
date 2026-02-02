from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v23.common.types.goal_common import (
    CustomerLifecycleOptimizationValueSettings,
)

_M = TypeVar("_M")

class GoalSetting(proto.Message):
    class RetentionGoal(proto.Message):
        value_settings: CustomerLifecycleOptimizationValueSettings
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            value_settings: CustomerLifecycleOptimizationValueSettings = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["value_settings"]
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
