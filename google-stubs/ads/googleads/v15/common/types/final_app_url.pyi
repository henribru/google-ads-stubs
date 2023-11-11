from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.enums.types.app_url_operating_system_type import (
    AppUrlOperatingSystemTypeEnum,
)

_M = TypeVar("_M")

class FinalAppUrl(proto.Message):
    os_type: AppUrlOperatingSystemTypeEnum.AppUrlOperatingSystemType
    url: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        os_type: AppUrlOperatingSystemTypeEnum.AppUrlOperatingSystemType = ...,
        url: str = ...
    ) -> None: ...
