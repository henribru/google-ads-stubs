from typing import Any

import proto

class FeedItemSetLink(proto.Message):
    resource_name: str
    feed_item: str
    feed_item_set: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        feed_item: str = ...,
        feed_item_set: str = ...
    ) -> None: ...
