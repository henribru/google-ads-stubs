from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class FeedMappingErrorEnum(proto.Message):
    class FeedMappingError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_PLACEHOLDER_FIELD = 2
        INVALID_CRITERION_FIELD = 3
        INVALID_PLACEHOLDER_TYPE = 4
        INVALID_CRITERION_TYPE = 5
        NO_ATTRIBUTE_FIELD_MAPPINGS = 7
        FEED_ATTRIBUTE_TYPE_MISMATCH = 8
        CANNOT_OPERATE_ON_MAPPINGS_FOR_SYSTEM_GENERATED_FEED = 9
        MULTIPLE_MAPPINGS_FOR_PLACEHOLDER_TYPE = 10
        MULTIPLE_MAPPINGS_FOR_CRITERION_TYPE = 11
        MULTIPLE_MAPPINGS_FOR_PLACEHOLDER_FIELD = 12
        MULTIPLE_MAPPINGS_FOR_CRITERION_FIELD = 13
        UNEXPECTED_ATTRIBUTE_FIELD_MAPPINGS = 14
        LOCATION_PLACEHOLDER_ONLY_FOR_PLACES_FEEDS = 15
        CANNOT_MODIFY_MAPPINGS_FOR_TYPED_FEED = 16
        INVALID_PLACEHOLDER_TYPE_FOR_NON_SYSTEM_GENERATED_FEED = 17
        INVALID_PLACEHOLDER_TYPE_FOR_SYSTEM_GENERATED_FEED_TYPE = 18
        ATTRIBUTE_FIELD_MAPPING_MISSING_FIELD = 19
        LEGACY_FEED_TYPE_READ_ONLY = 20

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
