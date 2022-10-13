from typing import Any

import proto

from google.ads.googleads.v10.enums.types.asset_group_status import AssetGroupStatusEnum

class AssetGroup(proto.Message):
    resource_name: str
    id: int
    campaign: str
    name: str
    final_urls: list[str]
    final_mobile_urls: list[str]
    status: AssetGroupStatusEnum.AssetGroupStatus
    path1: str
    path2: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        campaign: str = ...,
        name: str = ...,
        final_urls: list[str] = ...,
        final_mobile_urls: list[str] = ...,
        status: AssetGroupStatusEnum.AssetGroupStatus = ...,
        path1: str = ...,
        path2: str = ...
    ) -> None: ...
