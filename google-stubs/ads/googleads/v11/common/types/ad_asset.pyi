from typing import Any

import proto

from google.ads.googleads.v11.common.types.asset_policy import AdAssetPolicySummary
from google.ads.googleads.v11.enums.types.asset_performance_label import (
    AssetPerformanceLabelEnum,
)
from google.ads.googleads.v11.enums.types.served_asset_field_type import (
    ServedAssetFieldTypeEnum,
)

class AdDiscoveryCarouselCardAsset(proto.Message):
    asset: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        asset: str = ...
    ) -> None: ...

class AdImageAsset(proto.Message):
    asset: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        asset: str = ...
    ) -> None: ...

class AdMediaBundleAsset(proto.Message):
    asset: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        asset: str = ...
    ) -> None: ...

class AdTextAsset(proto.Message):
    text: str
    pinned_field: ServedAssetFieldTypeEnum.ServedAssetFieldType
    asset_performance_label: AssetPerformanceLabelEnum.AssetPerformanceLabel
    policy_summary_info: AdAssetPolicySummary
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        text: str = ...,
        pinned_field: ServedAssetFieldTypeEnum.ServedAssetFieldType = ...,
        asset_performance_label: AssetPerformanceLabelEnum.AssetPerformanceLabel = ...,
        policy_summary_info: AdAssetPolicySummary = ...
    ) -> None: ...

class AdVideoAsset(proto.Message):
    asset: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        asset: str = ...
    ) -> None: ...
