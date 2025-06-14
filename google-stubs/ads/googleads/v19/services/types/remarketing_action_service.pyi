import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.resources.types import remarketing_action
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateRemarketingActionsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['RemarketingActionOperation']
    partial_failure: bool
    validate_only: bool

class RemarketingActionOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: remarketing_action.RemarketingAction
    update: remarketing_action.RemarketingAction

class MutateRemarketingActionsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateRemarketingActionResult']

class MutateRemarketingActionResult(proto.Message):
    resource_name: str
