from typing import Any

import proto

__protobuf__: Any

class GeoTargetConstantSuggestionErrorEnum(proto.Message):
    class GeoTargetConstantSuggestionError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        LOCATION_NAME_SIZE_LIMIT: int
        LOCATION_NAME_LIMIT: int
        INVALID_COUNTRY_CODE: int
        REQUEST_PARAMETERS_UNSET: int
