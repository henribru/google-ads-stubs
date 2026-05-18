from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
