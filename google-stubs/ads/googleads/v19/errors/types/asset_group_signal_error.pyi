import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AssetGroupSignalErrorEnum(proto.Message):
    class AssetGroupSignalError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        TOO_MANY_WORDS: int
        SEARCH_THEME_POLICY_VIOLATION: int
        AUDIENCE_WITH_WRONG_ASSET_GROUP_ID: int
