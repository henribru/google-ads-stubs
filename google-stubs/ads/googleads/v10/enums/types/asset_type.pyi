from typing import Any

import proto

class AssetTypeEnum(proto.Message):
    class AssetType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        YOUTUBE_VIDEO = 2
        MEDIA_BUNDLE = 3
        IMAGE = 4
        TEXT = 5
        LEAD_FORM = 6
        BOOK_ON_GOOGLE = 7
        PROMOTION = 8
        CALLOUT = 9
        STRUCTURED_SNIPPET = 10
        SITELINK = 11
        PAGE_FEED = 12
        DYNAMIC_EDUCATION = 13
        MOBILE_APP = 14
        HOTEL_CALLOUT = 15
        CALL = 16
        PRICE = 17
        CALL_TO_ACTION = 18
        DYNAMIC_REAL_ESTATE = 19
        DYNAMIC_CUSTOM = 20
        DYNAMIC_HOTELS_AND_RENTALS = 21
        DYNAMIC_FLIGHTS = 22
        DISCOVERY_CAROUSEL_CARD = 23
        DYNAMIC_TRAVEL = 24
        DYNAMIC_LOCAL = 25
        DYNAMIC_JOBS = 26
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
