import proto
from _typeshed import Incomplete
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v11.resources.types import (
    ad_group_ad_label as ad_group_ad_label,
)

__protobuf__: Incomplete

class MutateAdGroupAdLabelsRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    partial_failure: Incomplete
    validate_only: Incomplete

class AdGroupAdLabelOperation(proto.Message):
    create: Incomplete
    remove: Incomplete

class MutateAdGroupAdLabelsResponse(proto.Message):
    partial_failure_error: Incomplete
    results: Incomplete

class MutateAdGroupAdLabelResult(proto.Message):
    resource_name: Incomplete
