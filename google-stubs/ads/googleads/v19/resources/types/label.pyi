from google.ads.googleads.v19.common.types.text_label import TextLabel
from google.ads.googleads.v19.enums.types.label_status import LabelStatusEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class Label(proto.Message):
    resource_name: str
    id: int
    name: str
    status: LabelStatusEnum.LabelStatus
    text_label: TextLabel
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ..., id: int = ..., name: str = ..., status: LabelStatusEnum.LabelStatus = ..., text_label: TextLabel = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "id", "name", "status", "text_label"]) -> bool: ...
