from google.ads.googleads.v18.enums.types.asset_field_type import AssetFieldTypeEnum
from google.ads.googleads.v18.enums.types.asset_source import AssetSourceEnum
from google.ads.googleads.v18.enums.types.advertising_channel_type import AdvertisingChannelTypeEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class ChannelAggregateAssetView(proto.Message):
    resource_name: str
    advertising_channel_type: AdvertisingChannelTypeEnum.AdvertisingChannelType
    asset: str
    asset_source: AssetSourceEnum.AssetSource
    field_type: AssetFieldTypeEnum.AssetFieldType
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ..., advertising_channel_type: AdvertisingChannelTypeEnum.AdvertisingChannelType = ..., asset: str = ..., asset_source: AssetSourceEnum.AssetSource = ..., field_type: AssetFieldTypeEnum.AssetFieldType = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "advertising_channel_type", "asset", "asset_source", "field_type"]) -> bool: ...
