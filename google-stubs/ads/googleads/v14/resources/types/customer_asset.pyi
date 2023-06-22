from collections.abc import MutableSequence
from typing import Any

import proto

from google.ads.googleads.v14.common.types.asset_policy import (
    AssetLinkPrimaryStatusDetails,
)
from google.ads.googleads.v14.enums.types.asset_field_type import AssetFieldTypeEnum
from google.ads.googleads.v14.enums.types.asset_link_primary_status import (
    AssetLinkPrimaryStatusEnum,
)
from google.ads.googleads.v14.enums.types.asset_link_primary_status_reason import (
    AssetLinkPrimaryStatusReasonEnum,
)
from google.ads.googleads.v14.enums.types.asset_link_status import AssetLinkStatusEnum
from google.ads.googleads.v14.enums.types.asset_source import AssetSourceEnum

class CustomerAsset(proto.Message):
    resource_name: str
    asset: str
    field_type: AssetFieldTypeEnum.AssetFieldType
    source: AssetSourceEnum.AssetSource
    status: AssetLinkStatusEnum.AssetLinkStatus
    primary_status: AssetLinkPrimaryStatusEnum.AssetLinkPrimaryStatus
    primary_status_details: MutableSequence[AssetLinkPrimaryStatusDetails]
    primary_status_reasons: MutableSequence[
        AssetLinkPrimaryStatusReasonEnum.AssetLinkPrimaryStatusReason
    ]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        asset: str = ...,
        field_type: AssetFieldTypeEnum.AssetFieldType = ...,
        source: AssetSourceEnum.AssetSource = ...,
        status: AssetLinkStatusEnum.AssetLinkStatus = ...,
        primary_status: AssetLinkPrimaryStatusEnum.AssetLinkPrimaryStatus = ...,
        primary_status_details: MutableSequence[AssetLinkPrimaryStatusDetails] = ...,
        primary_status_reasons: MutableSequence[
            AssetLinkPrimaryStatusReasonEnum.AssetLinkPrimaryStatusReason
        ] = ...
    ) -> None: ...
