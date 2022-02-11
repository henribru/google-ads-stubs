from typing import Any

import proto

__protobuf__: Any

class ThirdPartyAppAnalyticsLinkErrorEnum(proto.Message):
    class ThirdPartyAppAnalyticsLinkError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        INVALID_ANALYTICS_PROVIDER_ID: int
        INVALID_MOBILE_APP_ID: int
        MOBILE_APP_IS_NOT_ENABLED: int
        CANNOT_REGENERATE_SHAREABLE_LINK_ID_FOR_REMOVED_LINK: int
