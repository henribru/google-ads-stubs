import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.common.types import asset_policy
from google.ads.googleads.v20.enums.types import asset_performance_label as gage_asset_performance_label, served_asset_field_type

__protobuf__: Incomplete

class AdTextAsset(proto.Message):
    text: str
    pinned_field: served_asset_field_type.ServedAssetFieldTypeEnum.ServedAssetFieldType
    asset_performance_label: gage_asset_performance_label.AssetPerformanceLabelEnum.AssetPerformanceLabel
    policy_summary_info: asset_policy.AdAssetPolicySummary

class AdImageAsset(proto.Message):
    asset: str

class AdVideoAsset(proto.Message):
    asset: str
    ad_video_asset_info: AdVideoAssetInfo

class AdVideoAssetInfo(proto.Message):
    ad_video_asset_inventory_preferences: AdVideoAssetInventoryPreferences

class AdVideoAssetInventoryPreferences(proto.Message):
    in_feed_preference: bool
    in_stream_preference: bool
    shorts_preference: bool

class AdMediaBundleAsset(proto.Message):
    asset: str

class AdDemandGenCarouselCardAsset(proto.Message):
    asset: str

class AdCallToActionAsset(proto.Message):
    asset: str

class AdAppDeepLinkAsset(proto.Message):
    asset: str
