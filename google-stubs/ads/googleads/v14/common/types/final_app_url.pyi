from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v14.enums.types.app_url_operating_system_type import (
    AppUrlOperatingSystemTypeEnum,
)

_M = TypeVar("_M")

class FinalAppUrl(proto.Message):
    os_type: AppUrlOperatingSystemTypeEnum.AppUrlOperatingSystemType
    url: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        os_type: AppUrlOperatingSystemTypeEnum.AppUrlOperatingSystemType = ...,
        url: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["os_type", "url"]
    ) -> bool: ...
