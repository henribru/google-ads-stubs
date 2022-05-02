import proto
from _typeshed import Incomplete
from google.protobuf import field_mask_pb2 as field_mask_pb2

from google.ads.googleads.v10.resources.types import custom_interest as custom_interest

__protobuf__: Incomplete

class MutateCustomInterestsRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    validate_only: Incomplete

class CustomInterestOperation(proto.Message):
    update_mask: Incomplete
    create: Incomplete
    update: Incomplete

class MutateCustomInterestsResponse(proto.Message):
    results: Incomplete

class MutateCustomInterestResult(proto.Message):
    resource_name: Incomplete
