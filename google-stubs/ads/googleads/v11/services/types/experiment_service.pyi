import proto
from _typeshed import Incomplete
from google.protobuf import field_mask_pb2 as field_mask_pb2
from google.rpc import status_pb2 as status_pb2

__protobuf__: Incomplete

class MutateExperimentsRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    partial_failure: Incomplete
    validate_only: Incomplete

class ExperimentOperation(proto.Message):
    update_mask: Incomplete
    create: Incomplete
    update: Incomplete
    remove: Incomplete

class MutateExperimentsResponse(proto.Message):
    partial_failure_error: Incomplete
    results: Incomplete

class MutateExperimentResult(proto.Message):
    resource_name: Incomplete

class EndExperimentRequest(proto.Message):
    experiment: Incomplete
    validate_only: Incomplete

class ListExperimentAsyncErrorsRequest(proto.Message):
    resource_name: Incomplete
    page_token: Incomplete
    page_size: Incomplete

class ListExperimentAsyncErrorsResponse(proto.Message):
    @property
    def raw_page(self): ...
    errors: Incomplete
    next_page_token: Incomplete

class GraduateExperimentRequest(proto.Message):
    experiment: Incomplete
    campaign_budget_mappings: Incomplete
    validate_only: Incomplete

class CampaignBudgetMapping(proto.Message):
    experiment_campaign: Incomplete
    campaign_budget: Incomplete

class ScheduleExperimentRequest(proto.Message):
    resource_name: Incomplete
    validate_only: Incomplete

class ScheduleExperimentMetadata(proto.Message):
    experiment: Incomplete

class PromoteExperimentRequest(proto.Message):
    resource_name: Incomplete
    validate_only: Incomplete

class PromoteExperimentMetadata(proto.Message):
    experiment: Incomplete
