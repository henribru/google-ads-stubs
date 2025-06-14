from collections.abc import MutableSequence
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class TopicConstant(proto.Message):
    resource_name: str
    id: int
    topic_constant_parent: str
    path: MutableSequence[str]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ..., id: int = ..., topic_constant_parent: str = ..., path: MutableSequence[str] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "id", "topic_constant_parent", "path"]) -> bool: ...
