from typing import Any

import proto

__protobuf__: Any

class AssetFieldTypeEnum(proto.Message):
    class AssetFieldType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        HEADLINE: int
        DESCRIPTION: int
        MANDATORY_AD_TEXT: int
        MARKETING_IMAGE: int
        MEDIA_BUNDLE: int
        YOUTUBE_VIDEO: int
        BOOK_ON_GOOGLE: int
        LEAD_FORM: int
        PROMOTION: int
        CALLOUT: int
        STRUCTURED_SNIPPET: int
        SITELINK: int
        MOBILE_APP: int
        HOTEL_CALLOUT: int
        CALL: int
        PRICE: int
        LONG_HEADLINE: int
        BUSINESS_NAME: int
        SQUARE_MARKETING_IMAGE: int
        PORTRAIT_MARKETING_IMAGE: int
        LOGO: int
        LANDSCAPE_LOGO: int
        VIDEO: int
        CALL_TO_ACTION_SELECTION: int
