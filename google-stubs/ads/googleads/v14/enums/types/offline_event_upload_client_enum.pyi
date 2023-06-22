from typing import Any

import proto

class OfflineEventUploadClientEnum(proto.Message):
    class OfflineEventUploadClient(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        GOOGLE_ADS_API = 2
        GOOGLE_ADS_WEB_CLIENT = 3
        ADS_DATA_CONNECTOR = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
