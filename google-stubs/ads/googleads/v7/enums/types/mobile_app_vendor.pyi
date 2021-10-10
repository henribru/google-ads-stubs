from typing import Any

import proto

__protobuf__: Any

class MobileAppVendorEnum(proto.Message):
    class MobileAppVendor(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        APPLE_APP_STORE: int
        GOOGLE_APP_STORE: int
