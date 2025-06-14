import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ShareablePreviewErrorEnum(proto.Message):
    class ShareablePreviewError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        TOO_MANY_ASSET_GROUPS_IN_REQUEST: int
        ASSET_GROUP_DOES_NOT_EXIST_UNDER_THIS_CUSTOMER: int
