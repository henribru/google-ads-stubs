import proto
from _typeshed import Incomplete
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v11.resources.types import customer_label as customer_label

__protobuf__: Incomplete

class MutateCustomerLabelsRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    partial_failure: Incomplete
    validate_only: Incomplete

class CustomerLabelOperation(proto.Message):
    create: Incomplete
    remove: Incomplete

class MutateCustomerLabelsResponse(proto.Message):
    partial_failure_error: Incomplete
    results: Incomplete

class MutateCustomerLabelResult(proto.Message):
    resource_name: Incomplete
