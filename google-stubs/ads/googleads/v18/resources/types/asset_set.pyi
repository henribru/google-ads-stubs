import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.common.types import asset_set_types
from google.ads.googleads.v18.enums.types import asset_set_status, asset_set_type

__protobuf__: Incomplete

class AssetSet(proto.Message):
    class MerchantCenterFeed(proto.Message):
        merchant_id: int
        feed_label: str
    class HotelPropertyData(proto.Message):
        hotel_center_id: int
        partner_name: str
    id: int
    resource_name: str
    name: str
    type_: asset_set_type.AssetSetTypeEnum.AssetSetType
    status: asset_set_status.AssetSetStatusEnum.AssetSetStatus
    merchant_center_feed: MerchantCenterFeed
    location_group_parent_asset_set_id: int
    hotel_property_data: HotelPropertyData
    location_set: asset_set_types.LocationSet
    business_profile_location_group: asset_set_types.BusinessProfileLocationGroup
    chain_location_group: asset_set_types.ChainLocationGroup
