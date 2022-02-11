from typing import Any

import proto

from google.ads.googleads.v9.common.types import criteria as criteria
from google.ads.googleads.v9.enums.types import (
    campaign_criterion_status as campaign_criterion_status,
    criterion_type as criterion_type,
)

__protobuf__: Any

class CampaignCriterion(proto.Message):
    resource_name: Any
    campaign: Any
    criterion_id: Any
    display_name: Any
    bid_modifier: Any
    negative: Any
    type_: Any
    status: Any
    keyword: Any
    placement: Any
    mobile_app_category: Any
    mobile_application: Any
    location: Any
    device: Any
    ad_schedule: Any
    age_range: Any
    gender: Any
    income_range: Any
    parental_status: Any
    user_list: Any
    youtube_video: Any
    youtube_channel: Any
    proximity: Any
    topic: Any
    listing_scope: Any
    language: Any
    ip_block: Any
    content_label: Any
    carrier: Any
    user_interest: Any
    webpage: Any
    operating_system_version: Any
    mobile_device: Any
    location_group: Any
    custom_affinity: Any
    custom_audience: Any
    combined_audience: Any
    keyword_theme: Any
