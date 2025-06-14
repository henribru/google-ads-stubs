from google.ads.googleads.v18.enums.types.asset_set_link_status import AssetSetLinkStatusEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class CampaignAssetSet(proto.Message):
    resource_name: str
    campaign: str
    asset_set: str
    status: AssetSetLinkStatusEnum.AssetSetLinkStatus
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., campaign: str = ..., asset_set: str = ..., status: AssetSetLinkStatusEnum.AssetSetLinkStatus = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "campaign", "asset_set", "status"]) -> bool: ...
