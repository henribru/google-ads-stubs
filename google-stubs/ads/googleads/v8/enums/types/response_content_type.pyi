from typing import Any

import proto

__protobuf__: Any

class ResponseContentTypeEnum(proto.Message):
    class ResponseContentType(proto.Enum):
        UNSPECIFIED: int
        RESOURCE_NAME_ONLY: int
        MUTABLE_RESOURCE: int
