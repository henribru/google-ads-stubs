from typing import Any

import proto

from google.ads.googleads.v11.enums.types.campaign_experiment_status import (
    CampaignExperimentStatusEnum,
)
from google.ads.googleads.v11.enums.types.campaign_experiment_traffic_split_type import (
    CampaignExperimentTrafficSplitTypeEnum,
)

class CampaignExperiment(proto.Message):
    resource_name: str
    id: int
    campaign_draft: str
    name: str
    description: str
    traffic_split_percent: int
    traffic_split_type: CampaignExperimentTrafficSplitTypeEnum.CampaignExperimentTrafficSplitType
    experiment_campaign: str
    status: CampaignExperimentStatusEnum.CampaignExperimentStatus
    long_running_operation: str
    start_date: str
    end_date: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        campaign_draft: str = ...,
        name: str = ...,
        description: str = ...,
        traffic_split_percent: int = ...,
        traffic_split_type: CampaignExperimentTrafficSplitTypeEnum.CampaignExperimentTrafficSplitType = ...,
        experiment_campaign: str = ...,
        status: CampaignExperimentStatusEnum.CampaignExperimentStatus = ...,
        long_running_operation: str = ...,
        start_date: str = ...,
        end_date: str = ...
    ) -> None: ...
