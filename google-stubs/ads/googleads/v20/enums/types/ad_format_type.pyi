import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AdFormatTypeEnum(proto.Message):
    class AdFormatType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        OTHER: int
        UNSEGMENTED: int
        INSTREAM_SKIPPABLE: int
        INSTREAM_NON_SKIPPABLE: int
        INFEED: int
        BUMPER: int
        OUTSTREAM: int
        MASTHEAD: int
        AUDIO: int
        SHORTS: int
        PAUSE: int
