from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v13.common.types.text_label import TextLabel
from google.ads.googleads.v13.enums.types.label_status import LabelStatusEnum

_M = TypeVar("_M")

class Label(proto.Message):
    resource_name: str
    id: int
    name: str
    status: LabelStatusEnum.LabelStatus
    text_label: TextLabel
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        status: LabelStatusEnum.LabelStatus = ...,
        text_label: TextLabel = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name", "id", "name", "status", "text_label"]) -> bool: ...  # type: ignore[override]
