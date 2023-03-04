from typing import Any

import proto

class AppCampaignAppStoreEnum(proto.Message):
    class AppCampaignAppStore(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        APPLE_APP_STORE = 2
        GOOGLE_APP_STORE = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
