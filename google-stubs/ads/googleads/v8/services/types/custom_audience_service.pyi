from typing import Any

import proto
from google.protobuf import field_mask_pb2 as field_mask_pb2

from google.ads.googleads.v8.resources.types import custom_audience as custom_audience

__protobuf__: Any

class GetCustomAudienceRequest(proto.Message):
    resource_name: Any

class MutateCustomAudiencesRequest(proto.Message):
    customer_id: Any
    operations: Any
    validate_only: Any

class CustomAudienceOperation(proto.Message):
    update_mask: Any
    create: Any
    update: Any
    remove: Any

class MutateCustomAudiencesResponse(proto.Message):
    results: Any

class MutateCustomAudienceResult(proto.Message):
    resource_name: Any
