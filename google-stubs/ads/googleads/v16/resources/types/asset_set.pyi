from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v16.common.types.asset_set_types import (
    BusinessProfileLocationGroup,
    ChainLocationGroup,
    LocationSet,
)
from google.ads.googleads.v16.enums.types.asset_set_status import AssetSetStatusEnum
from google.ads.googleads.v16.enums.types.asset_set_type import AssetSetTypeEnum

_M = TypeVar("_M")

class AssetSet(proto.Message):
    class HotelPropertyData(proto.Message):
        hotel_center_id: int
        partner_name: str
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            hotel_center_id: int = ...,
            partner_name: str = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["hotel_center_id", "partner_name"]
        ) -> bool: ...

    class MerchantCenterFeed(proto.Message):
        merchant_id: int
        feed_label: str
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            merchant_id: int = ...,
            feed_label: str = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["merchant_id", "feed_label"]
        ) -> bool: ...

    id: int
    resource_name: str
    name: str
    type_: AssetSetTypeEnum.AssetSetType
    status: AssetSetStatusEnum.AssetSetStatus
    merchant_center_feed: AssetSet.MerchantCenterFeed
    location_group_parent_asset_set_id: int
    hotel_property_data: AssetSet.HotelPropertyData
    location_set: LocationSet
    business_profile_location_group: BusinessProfileLocationGroup
    chain_location_group: ChainLocationGroup
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        id: int = ...,
        resource_name: str = ...,
        name: str = ...,
        type_: AssetSetTypeEnum.AssetSetType = ...,
        status: AssetSetStatusEnum.AssetSetStatus = ...,
        merchant_center_feed: AssetSet.MerchantCenterFeed = ...,
        location_group_parent_asset_set_id: int = ...,
        hotel_property_data: AssetSet.HotelPropertyData = ...,
        location_set: LocationSet = ...,
        business_profile_location_group: BusinessProfileLocationGroup = ...,
        chain_location_group: ChainLocationGroup = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "id",
            "resource_name",
            "name",
            "type_",
            "status",
            "merchant_center_feed",
            "location_group_parent_asset_set_id",
            "hotel_property_data",
            "location_set",
            "business_profile_location_group",
            "chain_location_group",
        ],
    ) -> bool: ...
