from typing import Any

import proto

__protobuf__: Any

class ReachPlanAdLengthEnum(proto.Message):
    class ReachPlanAdLength(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        SIX_SECONDS: int
        FIFTEEN_OR_TWENTY_SECONDS: int
        TWENTY_SECONDS_OR_MORE: int
