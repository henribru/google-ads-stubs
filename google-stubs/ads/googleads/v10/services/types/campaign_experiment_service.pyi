import proto
from _typeshed import Incomplete
from google.protobuf import field_mask_pb2 as field_mask_pb2
from google.rpc import status_pb2 as status_pb2

__protobuf__: Incomplete

class MutateCampaignExperimentsRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    partial_failure: Incomplete
    validate_only: Incomplete
    response_content_type: Incomplete

class CampaignExperimentOperation(proto.Message):
    update_mask: Incomplete
    update: Incomplete
    remove: Incomplete

class MutateCampaignExperimentsResponse(proto.Message):
    partial_failure_error: Incomplete
    results: Incomplete

class MutateCampaignExperimentResult(proto.Message):
    resource_name: Incomplete
    campaign_experiment: Incomplete

class CreateCampaignExperimentRequest(proto.Message):
    customer_id: Incomplete
    campaign_experiment: Incomplete
    validate_only: Incomplete

class CreateCampaignExperimentMetadata(proto.Message):
    campaign_experiment: Incomplete

class GraduateCampaignExperimentRequest(proto.Message):
    campaign_experiment: Incomplete
    campaign_budget: Incomplete
    validate_only: Incomplete

class GraduateCampaignExperimentResponse(proto.Message):
    graduated_campaign: Incomplete

class PromoteCampaignExperimentRequest(proto.Message):
    campaign_experiment: Incomplete
    validate_only: Incomplete

class EndCampaignExperimentRequest(proto.Message):
    campaign_experiment: Incomplete
    validate_only: Incomplete

class ListCampaignExperimentAsyncErrorsRequest(proto.Message):
    resource_name: Incomplete
    page_token: Incomplete
    page_size: Incomplete

class ListCampaignExperimentAsyncErrorsResponse(proto.Message):
    @property
    def raw_page(self): ...
    errors: Incomplete
    next_page_token: Incomplete
