from typing import Any

import proto

__protobuf__: Any

class GetCampaignExperimentRequest(proto.Message):
    resource_name: Any

class MutateCampaignExperimentsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any
    response_content_type: Any

class CampaignExperimentOperation(proto.Message):
    update_mask: Any
    update: Any
    remove: Any

class MutateCampaignExperimentsResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateCampaignExperimentResult(proto.Message):
    resource_name: Any
    campaign_experiment: Any

class CreateCampaignExperimentRequest(proto.Message):
    customer_id: Any
    campaign_experiment: Any
    validate_only: Any

class CreateCampaignExperimentMetadata(proto.Message):
    campaign_experiment: Any

class GraduateCampaignExperimentRequest(proto.Message):
    campaign_experiment: Any
    campaign_budget: Any
    validate_only: Any

class GraduateCampaignExperimentResponse(proto.Message):
    graduated_campaign: Any

class PromoteCampaignExperimentRequest(proto.Message):
    campaign_experiment: Any
    validate_only: Any

class EndCampaignExperimentRequest(proto.Message):
    campaign_experiment: Any
    validate_only: Any

class ListCampaignExperimentAsyncErrorsRequest(proto.Message):
    resource_name: Any
    page_token: Any
    page_size: Any

class ListCampaignExperimentAsyncErrorsResponse(proto.Message):
    @property
    def raw_page(self): ...
    errors: Any
    next_page_token: Any
