import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AutomaticallyCreatedAssetRemovalErrorEnum(proto.Message):
    class AutomaticallyCreatedAssetRemovalError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        AD_DOES_NOT_EXIST: int
        INVALID_AD_TYPE: int
        ASSET_DOES_NOT_EXIST: int
        ASSET_FIELD_TYPE_DOES_NOT_MATCH: int
        NOT_AN_AUTOMATICALLY_CREATED_ASSET: int
