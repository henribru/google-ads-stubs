from typing import Any

import proto

__protobuf__: Any

class LegacyAppInstallAdAppStoreEnum(proto.Message):
    class LegacyAppInstallAdAppStore(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        APPLE_APP_STORE: int
        GOOGLE_PLAY: int
        WINDOWS_STORE: int
        WINDOWS_PHONE_STORE: int
        CN_APP_STORE: int
