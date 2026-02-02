from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v23.enums.types.asset_field_type import AssetFieldTypeEnum
from google.ads.googleads.v23.enums.types.asset_source import AssetSourceEnum

_M = TypeVar("_M")

class CampaignAggregateAssetView(proto.Message):
    resource_name: str
    campaign: str
    asset: str
    asset_source: AssetSourceEnum.AssetSource
    field_type: AssetFieldTypeEnum.AssetFieldType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        campaign: str = ...,
        asset: str = ...,
        asset_source: AssetSourceEnum.AssetSource = ...,
        field_type: AssetFieldTypeEnum.AssetFieldType = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name", "campaign", "asset", "asset_source", "field_type"
        ],
    ) -> bool: ...
