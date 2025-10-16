from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v22.enums.types.asset_field_type import AssetFieldTypeEnum
from google.ads.googleads.v22.enums.types.asset_link_status import AssetLinkStatusEnum

_M = TypeVar("_M")

class FinalUrlExpansionAssetView(proto.Message):
    resource_name: str
    campaign: str
    asset: str
    field_type: AssetFieldTypeEnum.AssetFieldType
    status: AssetLinkStatusEnum.AssetLinkStatus
    final_url: str
    ad_group: str
    asset_group: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        campaign: str = ...,
        asset: str = ...,
        field_type: AssetFieldTypeEnum.AssetFieldType = ...,
        status: AssetLinkStatusEnum.AssetLinkStatus = ...,
        final_url: str = ...,
        ad_group: str = ...,
        asset_group: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "campaign",
            "asset",
            "field_type",
            "status",
            "final_url",
            "ad_group",
            "asset_group",
        ],
    ) -> bool: ...
