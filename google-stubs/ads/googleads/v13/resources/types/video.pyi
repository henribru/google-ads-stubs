from typing import Any

import proto

class Video(proto.Message):
    resource_name: str
    id: str
    channel_id: str
    duration_millis: int
    title: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: str = ...,
        channel_id: str = ...,
        duration_millis: int = ...,
        title: str = ...
    ) -> None: ...
