from typing import Any

import proto

class AssetOfflineEvaluationErrorReasonsEnum(proto.Message):
    class AssetOfflineEvaluationErrorReasons(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        PRICE_ASSET_DESCRIPTION_REPEATS_ROW_HEADER = 2
        PRICE_ASSET_REPETITIVE_HEADERS = 3
        PRICE_ASSET_HEADER_INCOMPATIBLE_WITH_PRICE_TYPE = 4
        PRICE_ASSET_DESCRIPTION_INCOMPATIBLE_WITH_ITEM_HEADER = 5
        PRICE_ASSET_DESCRIPTION_HAS_PRICE_QUALIFIER = 6
        PRICE_ASSET_UNSUPPORTED_LANGUAGE = 7
        PRICE_ASSET_OTHER_ERROR = 8
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
