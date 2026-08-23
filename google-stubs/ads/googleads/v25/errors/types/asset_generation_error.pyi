from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class AssetGenerationErrorEnum(proto.Message):
    class AssetGenerationError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NO_ASSETS_GENERATED = 2
        FINAL_URL_REQUIRED = 3
        GENERATION_CONTEXT_MISSING_FINAL_URL = 4
        FINAL_URL_SENSITIVE = 5
        FINAL_URL_UNSUPPORTED_LANGUAGE = 6
        FINAL_URL_UNAVAILABLE = 7
        CAMPAIGN_TYPE_REQUIRED = 8
        UNSUPPORTED_CAMPAIGN_TYPE = 9
        UNSUPPORTED_FIELD_TYPE = 10
        UNSUPPORTED_FIELD_TYPE_FOR_CAMPAIGN_TYPE = 11
        FREEFORM_PROMPT_UNSUPPORTED_LANGUAGE = 12
        FREEFORM_PROMPT_SENSITIVE = 13
        INPUT_IMAGE_FILE_SIZE_TOO_LARGE = 14
        INPUT_IMAGE_EMPTY = 15
        GENERATION_TYPE_REQUIRED = 16
        TOO_MANY_KEYWORDS = 17
        KEYWORD_INVALID_LENGTH = 18
        NO_VALID_KEYWORDS = 19
        FREEFORM_PROMPT_INVALID_LENGTH = 20
        FREEFORM_PROMPT_REFERENCES_CHILDREN = 21
        FREEFORM_PROMPT_REFERENCES_SPECIFIC_PEOPLE = 22
        FREEFORM_PROMPT_VIOLATES_ADS_POLICY = 23
        FREEFORM_PROMPT_BRAND_CONTENT = 24
        INPUT_IMAGE_DEPICTS_CHILDREN = 25
        INPUT_IMAGE_CONTAINS_BRAND_CONTENT = 26
        INPUT_IMAGE_SENSITIVE = 27
        INPUT_IMAGE_VIOLATES_POLICY = 28
        ALL_OUTPUT_IMAGES_FILTERED_OUT_CHILDREN_DEPICTION = 29
        ALL_OUTPUT_IMAGES_FILTERED_OUT_SPECIFIC_PEOPLE = 30
        ALL_OUTPUT_IMAGES_FILTERED_OUT = 31
        INPUT_IMAGE_REQUIRED = 32
        INPUT_IMAGE_UNSUPPORTED_IMAGE_TYPE = 33
        CONTEXT_ASSET_GROUP_NOT_FOUND = 34
        CONTEXT_AD_GROUP_AD_NOT_FOUND = 35
        CONTEXT_CAMPAIGN_NOT_FOUND = 36

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
