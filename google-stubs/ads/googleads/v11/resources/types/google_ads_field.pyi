from typing import Any

import proto

from google.ads.googleads.v11.enums.types.google_ads_field_category import (
    GoogleAdsFieldCategoryEnum,
)
from google.ads.googleads.v11.enums.types.google_ads_field_data_type import (
    GoogleAdsFieldDataTypeEnum,
)

class GoogleAdsField(proto.Message):
    resource_name: str
    name: str
    category: GoogleAdsFieldCategoryEnum.GoogleAdsFieldCategory
    selectable: bool
    filterable: bool
    sortable: bool
    selectable_with: list[str]
    attribute_resources: list[str]
    metrics: list[str]
    segments: list[str]
    enum_values: list[str]
    data_type: GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType
    type_url: str
    is_repeated: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        name: str = ...,
        category: GoogleAdsFieldCategoryEnum.GoogleAdsFieldCategory = ...,
        selectable: bool = ...,
        filterable: bool = ...,
        sortable: bool = ...,
        selectable_with: list[str] = ...,
        attribute_resources: list[str] = ...,
        metrics: list[str] = ...,
        segments: list[str] = ...,
        enum_values: list[str] = ...,
        data_type: GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType = ...,
        type_url: str = ...,
        is_repeated: bool = ...
    ) -> None: ...
