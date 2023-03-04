from typing import Any

import proto

class AdGroupCriterionLabel(proto.Message):
    resource_name: str
    ad_group_criterion: str
    label: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        ad_group_criterion: str = ...,
        label: str = ...
    ) -> None: ...
