from typing import Any

import proto

__protobuf__: Any

class ConversionAdjustmentUploadErrorEnum(proto.Message):
    class ConversionAdjustmentUploadError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        TOO_RECENT_CONVERSION_ACTION: int
        INVALID_CONVERSION_ACTION: int
        CONVERSION_ALREADY_RETRACTED: int
        CONVERSION_NOT_FOUND: int
        CONVERSION_EXPIRED: int
        ADJUSTMENT_PRECEDES_CONVERSION: int
        MORE_RECENT_RESTATEMENT_FOUND: int
        TOO_RECENT_CONVERSION: int
        CANNOT_RESTATE_CONVERSION_ACTION_THAT_ALWAYS_USES_DEFAULT_CONVERSION_VALUE: int
        TOO_MANY_ADJUSTMENTS_IN_REQUEST: int
        TOO_MANY_ADJUSTMENTS: int
