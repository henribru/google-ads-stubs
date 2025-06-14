import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ResponseContentTypeEnum(proto.Message):
    class ResponseContentType(proto.Enum):
        UNSPECIFIED: int
        RESOURCE_NAME_ONLY: int
        MUTABLE_RESOURCE: int
