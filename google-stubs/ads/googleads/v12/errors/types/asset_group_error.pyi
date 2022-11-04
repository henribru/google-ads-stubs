from typing import Any

import proto

class AssetGroupErrorEnum(proto.Message):
    class AssetGroupError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DUPLICATE_NAME = 2
        CANNOT_ADD_ASSET_GROUP_FOR_CAMPAIGN_TYPE = 3
        NOT_ENOUGH_HEADLINE_ASSET = 4
        NOT_ENOUGH_LONG_HEADLINE_ASSET = 5
        NOT_ENOUGH_DESCRIPTION_ASSET = 6
        NOT_ENOUGH_BUSINESS_NAME_ASSET = 7
        NOT_ENOUGH_MARKETING_IMAGE_ASSET = 8
        NOT_ENOUGH_SQUARE_MARKETING_IMAGE_ASSET = 9
        NOT_ENOUGH_LOGO_ASSET = 10
        FINAL_URL_SHOPPING_MERCHANT_HOME_PAGE_URL_DOMAINS_DIFFER = 11
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
