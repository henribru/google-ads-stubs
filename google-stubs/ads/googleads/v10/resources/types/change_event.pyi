from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask

from google.ads.googleads.v10.enums.types.change_client_type import ChangeClientTypeEnum
from google.ads.googleads.v10.enums.types.change_event_resource_type import (
    ChangeEventResourceTypeEnum,
)
from google.ads.googleads.v10.enums.types.resource_change_operation import (
    ResourceChangeOperationEnum,
)
from google.ads.googleads.v10.resources.types.ad import Ad
from google.ads.googleads.v10.resources.types.ad_group import AdGroup
from google.ads.googleads.v10.resources.types.ad_group_ad import AdGroupAd
from google.ads.googleads.v10.resources.types.ad_group_asset import AdGroupAsset
from google.ads.googleads.v10.resources.types.ad_group_bid_modifier import (
    AdGroupBidModifier,
)
from google.ads.googleads.v10.resources.types.ad_group_criterion import AdGroupCriterion
from google.ads.googleads.v10.resources.types.ad_group_feed import AdGroupFeed
from google.ads.googleads.v10.resources.types.asset import Asset
from google.ads.googleads.v10.resources.types.asset_set import AssetSet
from google.ads.googleads.v10.resources.types.asset_set_asset import AssetSetAsset
from google.ads.googleads.v10.resources.types.campaign import Campaign
from google.ads.googleads.v10.resources.types.campaign_asset import CampaignAsset
from google.ads.googleads.v10.resources.types.campaign_asset_set import CampaignAssetSet
from google.ads.googleads.v10.resources.types.campaign_budget import CampaignBudget
from google.ads.googleads.v10.resources.types.campaign_criterion import (
    CampaignCriterion,
)
from google.ads.googleads.v10.resources.types.campaign_feed import CampaignFeed
from google.ads.googleads.v10.resources.types.customer_asset import CustomerAsset
from google.ads.googleads.v10.resources.types.feed import Feed
from google.ads.googleads.v10.resources.types.feed_item import FeedItem

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
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
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
            campaign_asset_set: CampaignAssetSet = ...
        ) -> None: ...
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
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
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
        asset: str = ...
    ) -> None: ...
