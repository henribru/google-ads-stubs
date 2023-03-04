from collections.abc import MutableSequence
from typing import Any

import proto

class TopicConstant(proto.Message):
    resource_name: str
    id: int
    topic_constant_parent: str
    path: MutableSequence[str]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        topic_constant_parent: str = ...,
        path: MutableSequence[str] = ...
    ) -> None: ...
