from typing import Any

import proto

from google.ads.googleads.v11.enums.types.app_url_operating_system_type import (
    AppUrlOperatingSystemTypeEnum,
)

class FinalAppUrl(proto.Message):
    os_type: AppUrlOperatingSystemTypeEnum.AppUrlOperatingSystemType
    url: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        os_type: AppUrlOperatingSystemTypeEnum.AppUrlOperatingSystemType = ...,
        url: str = ...
    ) -> None: ...
