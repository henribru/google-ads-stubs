from typing import Any

import proto

class CustomerAcquisitionOptimizationModeEnum(proto.Message):
    class CustomerAcquisitionOptimizationMode(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        TARGET_ALL_EQUALLY = 2
        BID_HIGHER_FOR_NEW_CUSTOMER = 3
        TARGET_NEW_CUSTOMER = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
