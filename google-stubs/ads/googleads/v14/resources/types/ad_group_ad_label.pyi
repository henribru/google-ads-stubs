from typing import Any

import proto

class AdGroupAdLabel(proto.Message):
    resource_name: str
    ad_group_ad: str
    label: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        ad_group_ad: str = ...,
        label: str = ...
    ) -> None: ...
