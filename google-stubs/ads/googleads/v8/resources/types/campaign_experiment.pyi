from typing import Any

import proto

from google.ads.googleads.v8.enums.types import (
    campaign_experiment_status as campaign_experiment_status,
    campaign_experiment_traffic_split_type as campaign_experiment_traffic_split_type,
)

__protobuf__: Any

class CampaignExperiment(proto.Message):
    resource_name: Any
    id: Any
    campaign_draft: Any
    name: Any
    description: Any
    traffic_split_percent: Any
    traffic_split_type: Any
    experiment_campaign: Any
    status: Any
    long_running_operation: Any
    start_date: Any
    end_date: Any
