from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class ThirdPartyAppAnalyticsLinkErrorEnum(proto.Message):
    class ThirdPartyAppAnalyticsLinkError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_ANALYTICS_PROVIDER_ID = 2
        INVALID_MOBILE_APP_ID = 3
        MOBILE_APP_IS_NOT_ENABLED = 4
        CANNOT_REGENERATE_SHAREABLE_LINK_ID_FOR_REMOVED_LINK = 5

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
