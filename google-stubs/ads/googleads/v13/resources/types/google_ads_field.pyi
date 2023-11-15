from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v13.enums.types.google_ads_field_category import (
    GoogleAdsFieldCategoryEnum,
)
from google.ads.googleads.v13.enums.types.google_ads_field_data_type import (
    GoogleAdsFieldDataTypeEnum,
)

_M = TypeVar("_M")

class GoogleAdsField(proto.Message):
    resource_name: str
    name: str
    category: GoogleAdsFieldCategoryEnum.GoogleAdsFieldCategory
    selectable: bool
    filterable: bool
    sortable: bool
    selectable_with: MutableSequence[str]
    attribute_resources: MutableSequence[str]
    metrics: MutableSequence[str]
    segments: MutableSequence[str]
    enum_values: MutableSequence[str]
    data_type: GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType
    type_url: str
    is_repeated: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        name: str = ...,
        category: GoogleAdsFieldCategoryEnum.GoogleAdsFieldCategory = ...,
        selectable: bool = ...,
        filterable: bool = ...,
        sortable: bool = ...,
        selectable_with: MutableSequence[str] = ...,
        attribute_resources: MutableSequence[str] = ...,
        metrics: MutableSequence[str] = ...,
        segments: MutableSequence[str] = ...,
        enum_values: MutableSequence[str] = ...,
        data_type: GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType = ...,
        type_url: str = ...,
        is_repeated: bool = ...
    ) -> None: ...
