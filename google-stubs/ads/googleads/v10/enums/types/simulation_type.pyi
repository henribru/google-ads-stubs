from typing import Any

import proto

class SimulationTypeEnum(proto.Message):
    class SimulationType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CPC_BID = 2
        CPV_BID = 3
        TARGET_CPA = 4
        BID_MODIFIER = 5
        TARGET_ROAS = 6
        PERCENT_CPC_BID = 7
        TARGET_IMPRESSION_SHARE = 8
        BUDGET = 9
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
