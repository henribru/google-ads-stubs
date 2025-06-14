import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.resources.types import ad_group_criterion_label
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateAdGroupCriterionLabelsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['AdGroupCriterionLabelOperation']
    partial_failure: bool
    validate_only: bool

class AdGroupCriterionLabelOperation(proto.Message):
    create: ad_group_criterion_label.AdGroupCriterionLabel
    remove: str

class MutateAdGroupCriterionLabelsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateAdGroupCriterionLabelResult']

class MutateAdGroupCriterionLabelResult(proto.Message):
    resource_name: str
