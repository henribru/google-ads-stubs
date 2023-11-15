from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class ExperimentArm(proto.Message):
    resource_name: str
    experiment: str
    name: str
    control: bool
    traffic_split: int
    campaigns: MutableSequence[str]
    in_design_campaigns: MutableSequence[str]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        experiment: str = ...,
        name: str = ...,
        control: bool = ...,
        traffic_split: int = ...,
        campaigns: MutableSequence[str] = ...,
        in_design_campaigns: MutableSequence[str] = ...
    ) -> None: ...
