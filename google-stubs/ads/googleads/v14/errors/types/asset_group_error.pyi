from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

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
        PATH1_REQUIRED_WHEN_PATH2_IS_SET = 12
        SHORT_DESCRIPTION_REQUIRED = 13
        FINAL_URL_REQUIRED = 14
        FINAL_URL_CONTAINS_INVALID_DOMAIN_NAME = 15
        AD_CUSTOMIZER_NOT_SUPPORTED = 16
        CANNOT_MUTATE_ASSET_GROUP_FOR_REMOVED_CAMPAIGN = 17

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
