import proto
from _typeshed import Incomplete
from typing import MutableSequence

__protobuf__: Incomplete

class TopicConstant(proto.Message):
    resource_name: str
    id: int
    topic_constant_parent: str
    path: MutableSequence[str]
