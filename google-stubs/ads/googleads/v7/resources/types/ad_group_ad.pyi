from typing import Any

import proto

from google.ads.googleads.v7.enums.types import (
    ad_group_ad_status as ad_group_ad_status,
    policy_approval_status as policy_approval_status,
    policy_review_status as policy_review_status,
)

__protobuf__: Any

class AdGroupAd(proto.Message):
    resource_name: Any
    status: Any
    ad_group: Any
    ad: Any
    policy_summary: Any
    ad_strength: Any
    labels: Any

class AdGroupAdPolicySummary(proto.Message):
    policy_topic_entries: Any
    review_status: Any
    approval_status: Any
