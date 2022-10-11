import proto
from _typeshed import Incomplete
from google.protobuf import field_mask_pb2 as field_mask_pb2

from google.ads.googleads.v11.resources.types import custom_audience as custom_audience

__protobuf__: Incomplete

class MutateCustomAudiencesRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    validate_only: Incomplete

class CustomAudienceOperation(proto.Message):
    update_mask: Incomplete
    create: Incomplete
    update: Incomplete
    remove: Incomplete

class MutateCustomAudiencesResponse(proto.Message):
    results: Incomplete

class MutateCustomAudienceResult(proto.Message):
    resource_name: Incomplete
