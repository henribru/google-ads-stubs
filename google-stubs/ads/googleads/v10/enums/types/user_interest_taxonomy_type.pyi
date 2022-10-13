from typing import Any

import proto

class UserInterestTaxonomyTypeEnum(proto.Message):
    class UserInterestTaxonomyType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        AFFINITY = 2
        IN_MARKET = 3
        MOBILE_APP_INSTALL_USER = 4
        VERTICAL_GEO = 5
        NEW_SMART_PHONE_USER = 6
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
