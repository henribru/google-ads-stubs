import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.resources.types import customer_label
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateCustomerLabelsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['CustomerLabelOperation']
    partial_failure: bool
    validate_only: bool

class CustomerLabelOperation(proto.Message):
    create: customer_label.CustomerLabel
    remove: str

class MutateCustomerLabelsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateCustomerLabelResult']

class MutateCustomerLabelResult(proto.Message):
    resource_name: str
