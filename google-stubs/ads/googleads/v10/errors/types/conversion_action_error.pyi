from typing import Any

import proto

class ConversionActionErrorEnum(proto.Message):
    class ConversionActionError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DUPLICATE_NAME = 2
        DUPLICATE_APP_ID = 3
        TWO_CONVERSION_ACTIONS_BIDDING_ON_SAME_APP_DOWNLOAD = 4
        BIDDING_ON_SAME_APP_DOWNLOAD_AS_GLOBAL_ACTION = 5
        DATA_DRIVEN_MODEL_WAS_NEVER_GENERATED = 6
        DATA_DRIVEN_MODEL_EXPIRED = 7
        DATA_DRIVEN_MODEL_STALE = 8
        DATA_DRIVEN_MODEL_UNKNOWN = 9
        CREATION_NOT_SUPPORTED = 10
        UPDATE_NOT_SUPPORTED = 11
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
