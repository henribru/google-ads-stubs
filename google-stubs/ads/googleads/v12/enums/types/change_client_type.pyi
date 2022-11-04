from typing import Any

import proto

class ChangeClientTypeEnum(proto.Message):
    class ChangeClientType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        GOOGLE_ADS_WEB_CLIENT = 2
        GOOGLE_ADS_AUTOMATED_RULE = 3
        GOOGLE_ADS_SCRIPTS = 4
        GOOGLE_ADS_BULK_UPLOAD = 5
        GOOGLE_ADS_API = 6
        GOOGLE_ADS_EDITOR = 7
        GOOGLE_ADS_MOBILE_APP = 8
        GOOGLE_ADS_RECOMMENDATIONS = 9
        SEARCH_ADS_360_SYNC = 10
        SEARCH_ADS_360_POST = 11
        INTERNAL_TOOL = 12
        OTHER = 13
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
