from typing import Any

import proto
from google.protobuf import field_mask_pb2 as field_mask_pb2

from google.ads.googleads.v8.resources.types import custom_interest as custom_interest

__protobuf__: Any

class GetCustomInterestRequest(proto.Message):
    resource_name: Any

class MutateCustomInterestsRequest(proto.Message):
    customer_id: Any
    operations: Any
    validate_only: Any

class CustomInterestOperation(proto.Message):
    update_mask: Any
    create: Any
    update: Any

class MutateCustomInterestsResponse(proto.Message):
    results: Any

class MutateCustomInterestResult(proto.Message):
    resource_name: Any
