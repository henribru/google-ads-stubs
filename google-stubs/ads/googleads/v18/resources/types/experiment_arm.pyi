from collections.abc import MutableSequence
from collections.abc import MutableSequence
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class ExperimentArm(proto.Message):
    resource_name: str
    experiment: str
    name: str
    control: bool
    traffic_split: int
    campaigns: MutableSequence[str]
    in_design_campaigns: MutableSequence[str]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., experiment: str = ..., name: str = ..., control: bool = ..., traffic_split: int = ..., campaigns: MutableSequence[str] = ..., in_design_campaigns: MutableSequence[str] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "experiment", "name", "control", "traffic_split", "campaigns", "in_design_campaigns"]) -> bool: ...
