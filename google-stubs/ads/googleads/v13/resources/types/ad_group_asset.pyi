from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v13.common.types.asset_policy import (
    AssetLinkPrimaryStatusDetails,
)
from google.ads.googleads.v13.enums.types.asset_field_type import AssetFieldTypeEnum
from google.ads.googleads.v13.enums.types.asset_link_primary_status import (
    AssetLinkPrimaryStatusEnum,
)
from google.ads.googleads.v13.enums.types.asset_link_primary_status_reason import (
    AssetLinkPrimaryStatusReasonEnum,
)
from google.ads.googleads.v13.enums.types.asset_link_status import AssetLinkStatusEnum
from google.ads.googleads.v13.enums.types.asset_source import AssetSourceEnum

_M = TypeVar("_M")

class AdGroupAsset(proto.Message):
    resource_name: str
    ad_group: str
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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        ad_group: str = ...,
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
