import proto
from _typeshed import Incomplete

from google.ads.googleads.v11.enums.types import (
    campaign_experiment_status as campaign_experiment_status,
    campaign_experiment_traffic_split_type as campaign_experiment_traffic_split_type,
)

__protobuf__: Incomplete

class CampaignExperiment(proto.Message):
    resource_name: Incomplete
    id: Incomplete
    campaign_draft: Incomplete
    name: Incomplete
    description: Incomplete
    traffic_split_percent: Incomplete
    traffic_split_type: Incomplete
    experiment_campaign: Incomplete
    status: Incomplete
    long_running_operation: Incomplete
    start_date: Incomplete
    end_date: Incomplete
