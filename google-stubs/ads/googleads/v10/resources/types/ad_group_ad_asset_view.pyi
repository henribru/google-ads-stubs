import proto
from _typeshed import Incomplete

from google.ads.googleads.v10.common.types import policy as policy
from google.ads.googleads.v10.enums.types import (
    asset_field_type as asset_field_type,
    asset_performance_label as asset_performance_label,
    policy_approval_status as policy_approval_status,
    policy_review_status as policy_review_status,
)

__protobuf__: Incomplete

class AdGroupAdAssetView(proto.Message):
    resource_name: Incomplete
    ad_group_ad: Incomplete
    asset: Incomplete
    field_type: Incomplete
    enabled: Incomplete
    policy_summary: Incomplete
    performance_label: Incomplete

class AdGroupAdAssetPolicySummary(proto.Message):
    policy_topic_entries: Incomplete
    review_status: Incomplete
    approval_status: Incomplete
