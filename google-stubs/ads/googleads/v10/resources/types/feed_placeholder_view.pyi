from typing import Any

import proto

from google.ads.googleads.v10.enums.types.placeholder_type import PlaceholderTypeEnum

class FeedPlaceholderView(proto.Message):
    resource_name: str
    placeholder_type: PlaceholderTypeEnum.PlaceholderType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        placeholder_type: PlaceholderTypeEnum.PlaceholderType = ...
    ) -> None: ...
