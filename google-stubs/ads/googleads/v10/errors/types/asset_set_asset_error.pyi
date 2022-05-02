import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AssetSetAssetErrorEnum(proto.Message):
    class AssetSetAssetError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        INVALID_ASSET_TYPE: int
        INVALID_ASSET_SET_TYPE: int
        DUPLICATE_EXTERNAL_KEY: int
