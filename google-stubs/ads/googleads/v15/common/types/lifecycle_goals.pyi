from typing import Any

import proto

class LifecycleGoalValueSettings(proto.Message):
    value: float
    high_lifetime_value: float
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        value: float = ...,
        high_lifetime_value: float = ...
    ) -> None: ...
