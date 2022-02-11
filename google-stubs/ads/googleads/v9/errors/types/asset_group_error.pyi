from typing import Any

import proto

__protobuf__: Any

class AssetGroupErrorEnum(proto.Message):
    class AssetGroupError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        DUPLICATE_NAME: int
        CANNOT_ADD_ASSET_GROUP_FOR_CAMPAIGN_TYPE: int
        NOT_ENOUGH_HEADLINE_ASSET: int
        NOT_ENOUGH_LONG_HEADLINE_ASSET: int
        NOT_ENOUGH_DESCRIPTION_ASSET: int
        NOT_ENOUGH_BUSINESS_NAME_ASSET: int
        NOT_ENOUGH_MARKETING_IMAGE_ASSET: int
        NOT_ENOUGH_SQUARE_MARKETING_IMAGE_ASSET: int
        NOT_ENOUGH_LOGO_ASSET: int
        FINAL_URL_SHOPPING_MERCHANT_HOME_PAGE_URL_DOMAINS_DIFFER: int
