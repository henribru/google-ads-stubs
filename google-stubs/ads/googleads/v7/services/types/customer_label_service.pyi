from typing import Any

import proto

from google.ads.googleads.v7.resources.types import customer_label as customer_label

__protobuf__: Any

class GetCustomerLabelRequest(proto.Message):
    resource_name: Any

class MutateCustomerLabelsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any

class CustomerLabelOperation(proto.Message):
    create: Any
    remove: Any

class MutateCustomerLabelsResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateCustomerLabelResult(proto.Message):
    resource_name: Any
