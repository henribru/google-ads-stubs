from typing import Any

import proto

from google.ads.googleads.v9.common.types import policy as policy
from google.ads.googleads.v9.enums.types import (
    asset_field_type as asset_field_type,
    asset_performance_label as asset_performance_label,
    policy_approval_status as policy_approval_status,
    policy_review_status as policy_review_status,
)

__protobuf__: Any

class AdGroupAdAssetView(proto.Message):
    resource_name: Any
    ad_group_ad: Any
    asset: Any
    field_type: Any
    enabled: Any
    policy_summary: Any
    performance_label: Any

class AdGroupAdAssetPolicySummary(proto.Message):
    policy_topic_entries: Any
    review_status: Any
    approval_status: Any
