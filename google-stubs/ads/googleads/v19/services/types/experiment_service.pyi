import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.resources.types import experiment as gagr_experiment
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateExperimentsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['ExperimentOperation']
    partial_failure: bool
    validate_only: bool

class ExperimentOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: gagr_experiment.Experiment
    update: gagr_experiment.Experiment
    remove: str

class MutateExperimentsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateExperimentResult']

class MutateExperimentResult(proto.Message):
    resource_name: str

class EndExperimentRequest(proto.Message):
    experiment: str
    validate_only: bool

class ListExperimentAsyncErrorsRequest(proto.Message):
    resource_name: str
    page_token: str
    page_size: int

class ListExperimentAsyncErrorsResponse(proto.Message):
    @property
    def raw_page(self): ...
    errors: MutableSequence[status_pb2.Status]
    next_page_token: str

class GraduateExperimentRequest(proto.Message):
    experiment: str
    campaign_budget_mappings: MutableSequence['CampaignBudgetMapping']
    validate_only: bool

class CampaignBudgetMapping(proto.Message):
    experiment_campaign: str
    campaign_budget: str

class ScheduleExperimentRequest(proto.Message):
    resource_name: str
    validate_only: bool

class ScheduleExperimentMetadata(proto.Message):
    experiment: str

class PromoteExperimentRequest(proto.Message):
    resource_name: str
    validate_only: bool

class PromoteExperimentMetadata(proto.Message):
    experiment: str
