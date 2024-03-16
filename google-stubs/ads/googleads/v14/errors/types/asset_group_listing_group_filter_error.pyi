from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class AssetGroupListingGroupFilterErrorEnum(proto.Message):
    class AssetGroupListingGroupFilterError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        TREE_TOO_DEEP = 2
        UNIT_CANNOT_HAVE_CHILDREN = 3
        SUBDIVISION_MUST_HAVE_EVERYTHING_ELSE_CHILD = 4
        DIFFERENT_DIMENSION_TYPE_BETWEEN_SIBLINGS = 5
        SAME_DIMENSION_VALUE_BETWEEN_SIBLINGS = 6
        SAME_DIMENSION_TYPE_BETWEEN_ANCESTORS = 7
        MULTIPLE_ROOTS = 8
        INVALID_DIMENSION_VALUE = 9
        MUST_REFINE_HIERARCHICAL_PARENT_TYPE = 10
        INVALID_PRODUCT_BIDDING_CATEGORY = 11
        CHANGING_CASE_VALUE_WITH_CHILDREN = 12
        SUBDIVISION_HAS_CHILDREN = 13
        CANNOT_REFINE_HIERARCHICAL_EVERYTHING_ELSE = 14

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
