import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class NewResourceCreationErrorEnum(proto.Message):
    class NewResourceCreationError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CANNOT_SET_ID_FOR_CREATE: int
        DUPLICATE_TEMP_IDS: int
        TEMP_ID_RESOURCE_HAD_ERRORS: int
