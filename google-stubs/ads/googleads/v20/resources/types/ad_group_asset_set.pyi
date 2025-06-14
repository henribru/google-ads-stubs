import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import asset_set_link_status

__protobuf__: Incomplete

class AdGroupAssetSet(proto.Message):
    resource_name: str
    ad_group: str
    asset_set: str
    status: asset_set_link_status.AssetSetLinkStatusEnum.AssetSetLinkStatus
