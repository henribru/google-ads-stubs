from typing import Any

import proto

from google.ads.googleads.v7.resources.types import (
    ad_group_criterion_label as ad_group_criterion_label,
)

__protobuf__: Any

class GetAdGroupCriterionLabelRequest(proto.Message):
    resource_name: Any

class MutateAdGroupCriterionLabelsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any

class AdGroupCriterionLabelOperation(proto.Message):
    create: Any
    remove: Any

class MutateAdGroupCriterionLabelsResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateAdGroupCriterionLabelResult(proto.Message):
    resource_name: Any
