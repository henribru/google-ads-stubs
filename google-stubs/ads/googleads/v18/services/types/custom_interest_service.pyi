import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.resources.types import custom_interest
from google.protobuf import field_mask_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateCustomInterestsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['CustomInterestOperation']
    validate_only: bool

class CustomInterestOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: custom_interest.CustomInterest
    update: custom_interest.CustomInterest

class MutateCustomInterestsResponse(proto.Message):
    results: MutableSequence['MutateCustomInterestResult']

class MutateCustomInterestResult(proto.Message):
    resource_name: str
