import proto
from _typeshed import Incomplete

from google.ads.googleads.v10.common.types import policy as policy
from google.ads.googleads.v10.enums.types import (
    ad_group_ad_status as ad_group_ad_status,
    policy_approval_status as policy_approval_status,
    policy_review_status as policy_review_status,
)

__protobuf__: Incomplete

class AdGroupAd(proto.Message):
    resource_name: Incomplete
    status: Incomplete
    ad_group: Incomplete
    ad: Incomplete
    policy_summary: Incomplete
    ad_strength: Incomplete
    action_items: Incomplete
    labels: Incomplete

class AdGroupAdPolicySummary(proto.Message):
    policy_topic_entries: Incomplete
    review_status: Incomplete
    approval_status: Incomplete
