import proto
from _typeshed import Incomplete
from typing import MutableSequence

__protobuf__: Incomplete

class ExperimentArm(proto.Message):
    resource_name: str
    experiment: str
    name: str
    control: bool
    traffic_split: int
    campaigns: MutableSequence[str]
    in_design_campaigns: MutableSequence[str]
