from typing import Any

import proto

from google.ads.googleads.v7.resources.types import ad_group_label as ad_group_label

__protobuf__: Any

class GetAdGroupLabelRequest(proto.Message):
    resource_name: Any

class MutateAdGroupLabelsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any

class AdGroupLabelOperation(proto.Message):
    create: Any
    remove: Any

class MutateAdGroupLabelsResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateAdGroupLabelResult(proto.Message):
    resource_name: Any
