import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AssetSetErrorEnum(proto.Message):
    class AssetSetError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        DUPLICATE_ASSET_SET_NAME: int
        INVALID_PARENT_ASSET_SET_TYPE: int
        ASSET_SET_SOURCE_INCOMPATIBLE_WITH_PARENT_ASSET_SET: int
        ASSET_SET_TYPE_CANNOT_BE_LINKED_TO_CUSTOMER: int
        INVALID_CHAIN_IDS: int
        LOCATION_SYNC_ASSET_SET_DOES_NOT_SUPPORT_RELATIONSHIP_TYPE: int
        NOT_UNIQUE_ENABLED_LOCATION_SYNC_TYPED_ASSET_SET: int
        INVALID_PLACE_IDS: int
        OAUTH_INFO_INVALID: int
        OAUTH_INFO_MISSING: int
        CANNOT_DELETE_AS_ENABLED_LINKAGES_EXIST: int
