import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AssetOfflineEvaluationErrorReasonsEnum(proto.Message):
    class AssetOfflineEvaluationErrorReasons(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PRICE_ASSET_DESCRIPTION_REPEATS_ROW_HEADER: int
        PRICE_ASSET_REPETITIVE_HEADERS: int
        PRICE_ASSET_HEADER_INCOMPATIBLE_WITH_PRICE_TYPE: int
        PRICE_ASSET_DESCRIPTION_INCOMPATIBLE_WITH_ITEM_HEADER: int
        PRICE_ASSET_DESCRIPTION_HAS_PRICE_QUALIFIER: int
        PRICE_ASSET_UNSUPPORTED_LANGUAGE: int
        PRICE_ASSET_OTHER_ERROR: int
