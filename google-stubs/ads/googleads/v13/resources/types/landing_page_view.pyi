from typing import Any

import proto

class LandingPageView(proto.Message):
    resource_name: str
    unexpanded_final_url: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        unexpanded_final_url: str = ...
    ) -> None: ...
