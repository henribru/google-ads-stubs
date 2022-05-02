import proto
from _typeshed import Incomplete
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v10.resources.types import (
    ad_group_criterion_label as ad_group_criterion_label,
)

__protobuf__: Incomplete

class MutateAdGroupCriterionLabelsRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    partial_failure: Incomplete
    validate_only: Incomplete

class AdGroupCriterionLabelOperation(proto.Message):
    create: Incomplete
    remove: Incomplete

class MutateAdGroupCriterionLabelsResponse(proto.Message):
    partial_failure_error: Incomplete
    results: Incomplete

class MutateAdGroupCriterionLabelResult(proto.Message):
    resource_name: Incomplete
