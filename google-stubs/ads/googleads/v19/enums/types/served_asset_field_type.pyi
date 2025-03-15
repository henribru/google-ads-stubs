from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class ServedAssetFieldTypeEnum(proto.Message):
    class ServedAssetFieldType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        HEADLINE_1 = 2
        HEADLINE_2 = 3
        HEADLINE_3 = 4
        DESCRIPTION_1 = 5
        DESCRIPTION_2 = 6
        HEADLINE = 7
        HEADLINE_IN_PORTRAIT = 8
        LONG_HEADLINE = 9
        DESCRIPTION = 10
        DESCRIPTION_IN_PORTRAIT = 11
        BUSINESS_NAME_IN_PORTRAIT = 12
        BUSINESS_NAME = 13
        MARKETING_IMAGE = 14
        MARKETING_IMAGE_IN_PORTRAIT = 15
        SQUARE_MARKETING_IMAGE = 16
        PORTRAIT_MARKETING_IMAGE = 17
        LOGO = 18
        LANDSCAPE_LOGO = 19
        CALL_TO_ACTION = 20
        YOU_TUBE_VIDEO = 21
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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
