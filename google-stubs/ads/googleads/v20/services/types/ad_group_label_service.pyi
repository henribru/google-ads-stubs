import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.resources.types import ad_group_label
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateAdGroupLabelsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['AdGroupLabelOperation']
    partial_failure: bool
    validate_only: bool

class AdGroupLabelOperation(proto.Message):
    create: ad_group_label.AdGroupLabel
    remove: str

class MutateAdGroupLabelsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateAdGroupLabelResult']

class MutateAdGroupLabelResult(proto.Message):
    resource_name: str
