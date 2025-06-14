import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import asset_set_link_status

__protobuf__: Incomplete

class CampaignAssetSet(proto.Message):
    resource_name: str
    campaign: str
    asset_set: str
    status: asset_set_link_status.AssetSetLinkStatusEnum.AssetSetLinkStatus
