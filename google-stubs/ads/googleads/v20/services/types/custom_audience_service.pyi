import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.resources.types import custom_audience
from google.protobuf import field_mask_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateCustomAudiencesRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['CustomAudienceOperation']
    validate_only: bool

class CustomAudienceOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: custom_audience.CustomAudience
    update: custom_audience.CustomAudience
    remove: str

class MutateCustomAudiencesResponse(proto.Message):
    results: MutableSequence['MutateCustomAudienceResult']

class MutateCustomAudienceResult(proto.Message):
    resource_name: str
