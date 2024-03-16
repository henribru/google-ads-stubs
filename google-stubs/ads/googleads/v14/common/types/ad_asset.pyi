from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v14.common.types.asset_policy import AdAssetPolicySummary
from google.ads.googleads.v14.enums.types.asset_performance_label import (
    AssetPerformanceLabelEnum,
)
from google.ads.googleads.v14.enums.types.served_asset_field_type import (
    ServedAssetFieldTypeEnum,
)

_M = TypeVar("_M")

class AdCallToActionAsset(proto.Message):
    asset: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        asset: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["asset"]
    ) -> bool: ...

class AdDiscoveryCarouselCardAsset(proto.Message):
    asset: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        asset: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["asset"]
    ) -> bool: ...

class AdImageAsset(proto.Message):
    asset: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        asset: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["asset"]
    ) -> bool: ...

class AdMediaBundleAsset(proto.Message):
    asset: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        asset: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["asset"]
    ) -> bool: ...

class AdTextAsset(proto.Message):
    text: str
    pinned_field: ServedAssetFieldTypeEnum.ServedAssetFieldType
    asset_performance_label: AssetPerformanceLabelEnum.AssetPerformanceLabel
    policy_summary_info: AdAssetPolicySummary
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        text: str = ...,
        pinned_field: ServedAssetFieldTypeEnum.ServedAssetFieldType = ...,
        asset_performance_label: AssetPerformanceLabelEnum.AssetPerformanceLabel = ...,
        policy_summary_info: AdAssetPolicySummary = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "text", "pinned_field", "asset_performance_label", "policy_summary_info"
        ],
    ) -> bool: ...

class AdVideoAsset(proto.Message):
    asset: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        asset: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["asset"]
    ) -> bool: ...
