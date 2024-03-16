from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from typing_extensions import Literal

from google.ads.googleads.v15.enums.types.change_client_type import ChangeClientTypeEnum
from google.ads.googleads.v15.enums.types.change_event_resource_type import (
    ChangeEventResourceTypeEnum,
)
from google.ads.googleads.v15.enums.types.resource_change_operation import (
    ResourceChangeOperationEnum,
)
from google.ads.googleads.v15.resources.types.ad import Ad
from google.ads.googleads.v15.resources.types.ad_group import AdGroup
from google.ads.googleads.v15.resources.types.ad_group_ad import AdGroupAd
from google.ads.googleads.v15.resources.types.ad_group_asset import AdGroupAsset
from google.ads.googleads.v15.resources.types.ad_group_bid_modifier import (
    AdGroupBidModifier,
)
from google.ads.googleads.v15.resources.types.ad_group_criterion import AdGroupCriterion
from google.ads.googleads.v15.resources.types.ad_group_feed import AdGroupFeed
from google.ads.googleads.v15.resources.types.asset import Asset
from google.ads.googleads.v15.resources.types.asset_set import AssetSet
from google.ads.googleads.v15.resources.types.asset_set_asset import AssetSetAsset
from google.ads.googleads.v15.resources.types.campaign import Campaign
from google.ads.googleads.v15.resources.types.campaign_asset import CampaignAsset
from google.ads.googleads.v15.resources.types.campaign_asset_set import CampaignAssetSet
from google.ads.googleads.v15.resources.types.campaign_budget import CampaignBudget
from google.ads.googleads.v15.resources.types.campaign_criterion import (
    CampaignCriterion,
)
from google.ads.googleads.v15.resources.types.campaign_feed import CampaignFeed
from google.ads.googleads.v15.resources.types.customer_asset import CustomerAsset
from google.ads.googleads.v15.resources.types.feed import Feed
from google.ads.googleads.v15.resources.types.feed_item import FeedItem

_M = TypeVar("_M")

class ChangeEvent(proto.Message):
    class ChangedResource(proto.Message):
        ad: Ad
        ad_group: AdGroup
        ad_group_criterion: AdGroupCriterion
        campaign: Campaign
        campaign_budget: CampaignBudget
        ad_group_bid_modifier: AdGroupBidModifier
        campaign_criterion: CampaignCriterion
        feed: Feed
        feed_item: FeedItem
        campaign_feed: CampaignFeed
        ad_group_feed: AdGroupFeed
        ad_group_ad: AdGroupAd
        asset: Asset
        customer_asset: CustomerAsset
        campaign_asset: CampaignAsset
        ad_group_asset: AdGroupAsset
        asset_set: AssetSet
        asset_set_asset: AssetSetAsset
        campaign_asset_set: CampaignAssetSet
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            ad: Ad = ...,
            ad_group: AdGroup = ...,
            ad_group_criterion: AdGroupCriterion = ...,
            campaign: Campaign = ...,
            campaign_budget: CampaignBudget = ...,
            ad_group_bid_modifier: AdGroupBidModifier = ...,
            campaign_criterion: CampaignCriterion = ...,
            feed: Feed = ...,
            feed_item: FeedItem = ...,
            campaign_feed: CampaignFeed = ...,
            ad_group_feed: AdGroupFeed = ...,
            ad_group_ad: AdGroupAd = ...,
            asset: Asset = ...,
            customer_asset: CustomerAsset = ...,
            campaign_asset: CampaignAsset = ...,
            ad_group_asset: AdGroupAsset = ...,
            asset_set: AssetSet = ...,
            asset_set_asset: AssetSetAsset = ...,
            campaign_asset_set: CampaignAssetSet = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self,
            key: Literal[
                "ad",
                "ad_group",
                "ad_group_criterion",
                "campaign",
                "campaign_budget",
                "ad_group_bid_modifier",
                "campaign_criterion",
                "feed",
                "feed_item",
                "campaign_feed",
                "ad_group_feed",
                "ad_group_ad",
                "asset",
                "customer_asset",
                "campaign_asset",
                "ad_group_asset",
                "asset_set",
                "asset_set_asset",
                "campaign_asset_set",
            ],
        ) -> bool: ...

    resource_name: str
    change_date_time: str
    change_resource_type: ChangeEventResourceTypeEnum.ChangeEventResourceType
    change_resource_name: str
    client_type: ChangeClientTypeEnum.ChangeClientType
    user_email: str
    old_resource: ChangeEvent.ChangedResource
    new_resource: ChangeEvent.ChangedResource
    resource_change_operation: ResourceChangeOperationEnum.ResourceChangeOperation
    changed_fields: FieldMask
    campaign: str
    ad_group: str
    feed: str
    feed_item: str
    asset: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        change_date_time: str = ...,
        change_resource_type: ChangeEventResourceTypeEnum.ChangeEventResourceType = ...,
        change_resource_name: str = ...,
        client_type: ChangeClientTypeEnum.ChangeClientType = ...,
        user_email: str = ...,
        old_resource: ChangeEvent.ChangedResource = ...,
        new_resource: ChangeEvent.ChangedResource = ...,
        resource_change_operation: ResourceChangeOperationEnum.ResourceChangeOperation = ...,
        changed_fields: FieldMask = ...,
        campaign: str = ...,
        ad_group: str = ...,
        feed: str = ...,
        feed_item: str = ...,
        asset: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "change_date_time",
            "change_resource_type",
            "change_resource_name",
            "client_type",
            "user_email",
            "old_resource",
            "new_resource",
            "resource_change_operation",
            "changed_fields",
            "campaign",
            "ad_group",
            "feed",
            "feed_item",
            "asset",
        ],
    ) -> bool: ...
