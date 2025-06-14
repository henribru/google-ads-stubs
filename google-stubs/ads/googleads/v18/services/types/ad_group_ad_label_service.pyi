import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.resources.types import ad_group_ad_label
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateAdGroupAdLabelsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['AdGroupAdLabelOperation']
    partial_failure: bool
    validate_only: bool

class AdGroupAdLabelOperation(proto.Message):
    create: ad_group_ad_label.AdGroupAdLabel
    remove: str

class MutateAdGroupAdLabelsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateAdGroupAdLabelResult']

class MutateAdGroupAdLabelResult(proto.Message):
    resource_name: str
