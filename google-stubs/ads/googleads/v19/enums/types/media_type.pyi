import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class MediaTypeEnum(proto.Message):
    class MediaType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        IMAGE: int
        ICON: int
        MEDIA_BUNDLE: int
        AUDIO: int
        VIDEO: int
        DYNAMIC_IMAGE: int
