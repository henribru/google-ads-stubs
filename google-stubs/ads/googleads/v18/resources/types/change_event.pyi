import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import change_client_type, change_event_resource_type, resource_change_operation as gage_resource_change_operation
from google.ads.googleads.v18.resources.types import ad as gagr_ad, ad_group as gagr_ad_group, ad_group_ad as gagr_ad_group_ad, ad_group_asset as gagr_ad_group_asset, ad_group_bid_modifier as gagr_ad_group_bid_modifier, ad_group_criterion as gagr_ad_group_criterion, ad_group_feed as gagr_ad_group_feed, asset as gagr_asset, asset_set as gagr_asset_set, asset_set_asset as gagr_asset_set_asset, campaign as gagr_campaign, campaign_asset as gagr_campaign_asset, campaign_asset_set as gagr_campaign_asset_set, campaign_budget as gagr_campaign_budget, campaign_criterion as gagr_campaign_criterion, campaign_feed as gagr_campaign_feed, customer_asset as gagr_customer_asset, feed as gagr_feed, feed_item as gagr_feed_item
from google.protobuf import field_mask_pb2

__protobuf__: Incomplete

class ChangeEvent(proto.Message):
    class ChangedResource(proto.Message):
        ad: gagr_ad.Ad
        ad_group: gagr_ad_group.AdGroup
        ad_group_criterion: gagr_ad_group_criterion.AdGroupCriterion
        campaign: gagr_campaign.Campaign
        campaign_budget: gagr_campaign_budget.CampaignBudget
        ad_group_bid_modifier: gagr_ad_group_bid_modifier.AdGroupBidModifier
        campaign_criterion: gagr_campaign_criterion.CampaignCriterion
        feed: gagr_feed.Feed
        feed_item: gagr_feed_item.FeedItem
        campaign_feed: gagr_campaign_feed.CampaignFeed
        ad_group_feed: gagr_ad_group_feed.AdGroupFeed
        ad_group_ad: gagr_ad_group_ad.AdGroupAd
        asset: gagr_asset.Asset
        customer_asset: gagr_customer_asset.CustomerAsset
        campaign_asset: gagr_campaign_asset.CampaignAsset
        ad_group_asset: gagr_ad_group_asset.AdGroupAsset
        asset_set: gagr_asset_set.AssetSet
        asset_set_asset: gagr_asset_set_asset.AssetSetAsset
        campaign_asset_set: gagr_campaign_asset_set.CampaignAssetSet
    resource_name: str
    change_date_time: str
    change_resource_type: change_event_resource_type.ChangeEventResourceTypeEnum.ChangeEventResourceType
    change_resource_name: str
    client_type: change_client_type.ChangeClientTypeEnum.ChangeClientType
    user_email: str
    old_resource: ChangedResource
    new_resource: ChangedResource
    resource_change_operation: gage_resource_change_operation.ResourceChangeOperationEnum.ResourceChangeOperation
    changed_fields: field_mask_pb2.FieldMask
    campaign: str
    ad_group: str
    feed: str
    feed_item: str
    asset: str
