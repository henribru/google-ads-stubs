from typing import Any

import proto

class ReachPlanNetworkEnum(proto.Message):
    class ReachPlanNetwork(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        YOUTUBE = 2
        GOOGLE_VIDEO_PARTNERS = 3
        YOUTUBE_AND_GOOGLE_VIDEO_PARTNERS = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
