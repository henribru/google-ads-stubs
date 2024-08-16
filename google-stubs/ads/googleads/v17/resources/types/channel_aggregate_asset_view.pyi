from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v17.enums.types.advertising_channel_type import (
    AdvertisingChannelTypeEnum,
)
from google.ads.googleads.v17.enums.types.asset_field_type import AssetFieldTypeEnum
from google.ads.googleads.v17.enums.types.asset_source import AssetSourceEnum

_M = TypeVar("_M")

class ChannelAggregateAssetView(proto.Message):
    resource_name: str
    advertising_channel_type: AdvertisingChannelTypeEnum.AdvertisingChannelType
    asset: str
    asset_source: AssetSourceEnum.AssetSource
    field_type: AssetFieldTypeEnum.AssetFieldType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        advertising_channel_type: AdvertisingChannelTypeEnum.AdvertisingChannelType = ...,
        asset: str = ...,
        asset_source: AssetSourceEnum.AssetSource = ...,
        field_type: AssetFieldTypeEnum.AssetFieldType = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "advertising_channel_type",
            "asset",
            "asset_source",
            "field_type",
        ],
    ) -> bool: ...
