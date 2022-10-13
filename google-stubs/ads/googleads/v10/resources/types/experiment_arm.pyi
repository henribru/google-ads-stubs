from typing import Any

import proto

class ExperimentArm(proto.Message):
    resource_name: str
    trial: str
    name: str
    control: bool
    traffic_split: int
    campaigns: list[str]
    in_design_campaigns: list[str]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        trial: str = ...,
        name: str = ...,
        control: bool = ...,
        traffic_split: int = ...,
        campaigns: list[str] = ...,
        in_design_campaigns: list[str] = ...
    ) -> None: ...
