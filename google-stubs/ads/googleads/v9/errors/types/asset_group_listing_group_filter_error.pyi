from typing import Any

import proto

__protobuf__: Any

class AssetGroupListingGroupFilterErrorEnum(proto.Message):
    class AssetGroupListingGroupFilterError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        TREE_TOO_DEEP: int
        UNIT_CANNOT_HAVE_CHILDREN: int
        SUBDIVISION_MUST_HAVE_EVERYTHING_ELSE_CHILD: int
        DIFFERENT_DIMENSION_TYPE_BETWEEN_SIBLINGS: int
        SAME_DIMENSION_VALUE_BETWEEN_SIBLINGS: int
        SAME_DIMENSION_TYPE_BETWEEN_ANCESTORS: int
        MULTIPLE_ROOTS: int
        INVALID_DIMENSION_VALUE: int
        MUST_REFINE_HIERARCHICAL_PARENT_TYPE: int
        INVALID_PRODUCT_BIDDING_CATEGORY: int
        CHANGING_CASE_VALUE_WITH_CHILDREN: int
        SUBDIVISION_HAS_CHILDREN: int
        CANNOT_REFINE_HIERARCHICAL_EVERYTHING_ELSE: int
