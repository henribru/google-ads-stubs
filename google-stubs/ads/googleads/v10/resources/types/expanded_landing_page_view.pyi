from typing import Any

import proto

class ExpandedLandingPageView(proto.Message):
    resource_name: str
    expanded_final_url: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        expanded_final_url: str = ...
    ) -> None: ...
