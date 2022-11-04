from typing import Any

import proto

class PerStoreView(proto.Message):
    resource_name: str
    place_id: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        place_id: str = ...
    ) -> None: ...
