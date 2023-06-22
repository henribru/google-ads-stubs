from collections.abc import MutableSequence
from typing import Any

import proto

class ExperimentArm(proto.Message):
    resource_name: str
    experiment: str
    name: str
    control: bool
    traffic_split: int
    campaigns: MutableSequence[str]
    in_design_campaigns: MutableSequence[str]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        experiment: str = ...,
        name: str = ...,
        control: bool = ...,
        traffic_split: int = ...,
        campaigns: MutableSequence[str] = ...,
        in_design_campaigns: MutableSequence[str] = ...
    ) -> None: ...
