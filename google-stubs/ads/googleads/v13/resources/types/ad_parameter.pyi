from typing import Any

import proto

class AdParameter(proto.Message):
    resource_name: str
    ad_group_criterion: str
    parameter_index: int
    insertion_text: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        ad_group_criterion: str = ...,
        parameter_index: int = ...,
        insertion_text: str = ...
    ) -> None: ...
