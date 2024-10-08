from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class AutomaticallyCreatedAssetRemovalErrorEnum(proto.Message):
    class AutomaticallyCreatedAssetRemovalError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        AD_DOES_NOT_EXIST = 2
        INVALID_AD_TYPE = 3
        ASSET_DOES_NOT_EXIST = 4
        ASSET_FIELD_TYPE_DOES_NOT_MATCH = 5
        NOT_AN_AUTOMATICALLY_CREATED_ASSET = 6

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
