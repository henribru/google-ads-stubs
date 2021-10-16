from typing import Any

import proto

__protobuf__: Any

class ChangeClientTypeEnum(proto.Message):
    class ChangeClientType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        GOOGLE_ADS_WEB_CLIENT: int
        GOOGLE_ADS_AUTOMATED_RULE: int
        GOOGLE_ADS_SCRIPTS: int
        GOOGLE_ADS_BULK_UPLOAD: int
        GOOGLE_ADS_API: int
        GOOGLE_ADS_EDITOR: int
        GOOGLE_ADS_MOBILE_APP: int
        GOOGLE_ADS_RECOMMENDATIONS: int
        SEARCH_ADS_360_SYNC: int
        SEARCH_ADS_360_POST: int
        INTERNAL_TOOL: int
        OTHER: int
