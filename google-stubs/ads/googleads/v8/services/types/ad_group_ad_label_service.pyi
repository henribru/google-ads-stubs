from typing import Any

import proto
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v8.resources.types import (
    ad_group_ad_label as ad_group_ad_label,
)

__protobuf__: Any

class GetAdGroupAdLabelRequest(proto.Message):
    resource_name: Any

class MutateAdGroupAdLabelsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any

class AdGroupAdLabelOperation(proto.Message):
    create: Any
    remove: Any

class MutateAdGroupAdLabelsResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateAdGroupAdLabelResult(proto.Message):
    resource_name: Any
