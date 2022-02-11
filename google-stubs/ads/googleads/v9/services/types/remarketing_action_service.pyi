from typing import Any

import proto
from google.protobuf import field_mask_pb2 as field_mask_pb2
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v9.resources.types import (
    remarketing_action as remarketing_action,
)

__protobuf__: Any

class GetRemarketingActionRequest(proto.Message):
    resource_name: Any

class MutateRemarketingActionsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any

class RemarketingActionOperation(proto.Message):
    update_mask: Any
    create: Any
    update: Any

class MutateRemarketingActionsResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateRemarketingActionResult(proto.Message):
    resource_name: Any
