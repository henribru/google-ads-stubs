from typing import Any

import proto

from google.ads.googleads.v11.common.types.text_label import TextLabel
from google.ads.googleads.v11.enums.types.label_status import LabelStatusEnum

class Label(proto.Message):
    resource_name: str
    id: int
    name: str
    status: LabelStatusEnum.LabelStatus
    text_label: TextLabel
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        status: LabelStatusEnum.LabelStatus = ...,
        text_label: TextLabel = ...
    ) -> None: ...
