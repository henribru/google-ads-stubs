from typing import Any

import proto

class ServedAssetFieldTypeEnum(proto.Message):
    class ServedAssetFieldType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        HEADLINE_1 = 2
        HEADLINE_2 = 3
        HEADLINE_3 = 4
        DESCRIPTION_1 = 5
        DESCRIPTION_2 = 6
        SITELINK = 22
        CALL = 23
        MOBILE_APP = 24
        CALLOUT = 25
        STRUCTURED_SNIPPET = 26
        PRICE = 27
        PROMOTION = 28
        AD_IMAGE = 29
        LEAD_FORM = 30
        BUSINESS_LOGO = 31
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
