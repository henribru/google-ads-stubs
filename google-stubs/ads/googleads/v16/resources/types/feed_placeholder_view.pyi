from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v16.enums.types.placeholder_type import PlaceholderTypeEnum

_M = TypeVar("_M")

class FeedPlaceholderView(proto.Message):
    resource_name: str
    placeholder_type: PlaceholderTypeEnum.PlaceholderType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        placeholder_type: PlaceholderTypeEnum.PlaceholderType = ...,
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name", "placeholder_type"]) -> bool: ...  # type: ignore[override]