from collections.abc import MutableSequence
from typing import Any

import proto

from google.ads.googleads.v15.enums.types.ad_strength import AdStrengthEnum
from google.ads.googleads.v15.enums.types.asset_group_primary_status import (
    AssetGroupPrimaryStatusEnum,
)
from google.ads.googleads.v15.enums.types.asset_group_primary_status_reason import (
    AssetGroupPrimaryStatusReasonEnum,
)
from google.ads.googleads.v15.enums.types.asset_group_status import AssetGroupStatusEnum

class AssetGroup(proto.Message):
    resource_name: str
    id: int
    campaign: str
    name: str
    final_urls: MutableSequence[str]
    final_mobile_urls: MutableSequence[str]
    status: AssetGroupStatusEnum.AssetGroupStatus
    primary_status: AssetGroupPrimaryStatusEnum.AssetGroupPrimaryStatus
    primary_status_reasons: MutableSequence[
        AssetGroupPrimaryStatusReasonEnum.AssetGroupPrimaryStatusReason
    ]
    path1: str
    path2: str
    ad_strength: AdStrengthEnum.AdStrength
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        campaign: str = ...,
        name: str = ...,
        final_urls: MutableSequence[str] = ...,
        final_mobile_urls: MutableSequence[str] = ...,
        status: AssetGroupStatusEnum.AssetGroupStatus = ...,
        primary_status: AssetGroupPrimaryStatusEnum.AssetGroupPrimaryStatus = ...,
        primary_status_reasons: MutableSequence[
            AssetGroupPrimaryStatusReasonEnum.AssetGroupPrimaryStatusReason
        ] = ...,
        path1: str = ...,
        path2: str = ...,
        ad_strength: AdStrengthEnum.AdStrength = ...
    ) -> None: ...
