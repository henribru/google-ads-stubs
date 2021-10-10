from typing import Any

import proto

__protobuf__: Any

class AssetTypeEnum(proto.Message):
    class AssetType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        YOUTUBE_VIDEO: int
        MEDIA_BUNDLE: int
        IMAGE: int
        TEXT: int
        LEAD_FORM: int
        BOOK_ON_GOOGLE: int
        PROMOTION: int
        CALLOUT: int
        STRUCTURED_SNIPPET: int
        SITELINK: int
