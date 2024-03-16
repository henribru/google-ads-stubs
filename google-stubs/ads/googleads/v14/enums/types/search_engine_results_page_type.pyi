from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class SearchEngineResultsPageTypeEnum(proto.Message):
    class SearchEngineResultsPageType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ADS_ONLY = 2
        ORGANIC_ONLY = 3
        ADS_AND_ORGANIC = 4

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
