from typing import Any

import proto

from google.ads.googleads.v9.common.types import policy as policy
from google.ads.googleads.v9.enums.types import (
    policy_approval_status as policy_approval_status,
    policy_review_status as policy_review_status,
)

__protobuf__: Any

class AdAssetPolicySummary(proto.Message):
    policy_topic_entries: Any
    review_status: Any
    approval_status: Any
