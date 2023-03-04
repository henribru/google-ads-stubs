from typing import Any

import proto

class CampaignDraftStatusEnum(proto.Message):
    class CampaignDraftStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        PROPOSED = 2
        REMOVED = 3
        PROMOTING = 5
        PROMOTED = 4
        PROMOTE_FAILED = 6
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
