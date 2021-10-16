from typing import Any

import proto

__protobuf__: Any

class ConversionActionErrorEnum(proto.Message):
    class ConversionActionError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        DUPLICATE_NAME: int
        DUPLICATE_APP_ID: int
        TWO_CONVERSION_ACTIONS_BIDDING_ON_SAME_APP_DOWNLOAD: int
        BIDDING_ON_SAME_APP_DOWNLOAD_AS_GLOBAL_ACTION: int
        DATA_DRIVEN_MODEL_WAS_NEVER_GENERATED: int
        DATA_DRIVEN_MODEL_EXPIRED: int
        DATA_DRIVEN_MODEL_STALE: int
        DATA_DRIVEN_MODEL_UNKNOWN: int
        CREATION_NOT_SUPPORTED: int
        UPDATE_NOT_SUPPORTED: int
