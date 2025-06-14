import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import google_ads_field_category, google_ads_field_data_type
from typing import MutableSequence

__protobuf__: Incomplete

class GoogleAdsField(proto.Message):
    resource_name: str
    name: str
    category: google_ads_field_category.GoogleAdsFieldCategoryEnum.GoogleAdsFieldCategory
    selectable: bool
    filterable: bool
    sortable: bool
    selectable_with: MutableSequence[str]
    attribute_resources: MutableSequence[str]
    metrics: MutableSequence[str]
    segments: MutableSequence[str]
    enum_values: MutableSequence[str]
    data_type: google_ads_field_data_type.GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType
    type_url: str
    is_repeated: bool
