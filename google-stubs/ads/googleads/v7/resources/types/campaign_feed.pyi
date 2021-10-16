from typing import Any

import proto

from google.ads.googleads.v7.enums.types import (
    feed_link_status as feed_link_status,
    placeholder_type as placeholder_type,
)

__protobuf__: Any

class CampaignFeed(proto.Message):
    resource_name: Any
    feed: Any
    campaign: Any
    placeholder_types: Any
    matching_function: Any
    status: Any
