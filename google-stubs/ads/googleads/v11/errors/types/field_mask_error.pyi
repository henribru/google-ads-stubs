import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class FieldMaskErrorEnum(proto.Message):
    class FieldMaskError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        FIELD_MASK_MISSING: int
        FIELD_MASK_NOT_ALLOWED: int
        FIELD_NOT_FOUND: int
        FIELD_HAS_SUBFIELDS: int
