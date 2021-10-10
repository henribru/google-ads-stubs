from typing import Any

import proto

from google.ads.googleads.v7.resources.types import (
    customer_manager_link as customer_manager_link,
)

__protobuf__: Any

class GetCustomerManagerLinkRequest(proto.Message):
    resource_name: Any

class MutateCustomerManagerLinkRequest(proto.Message):
    customer_id: Any
    operations: Any
    validate_only: Any

class MoveManagerLinkRequest(proto.Message):
    customer_id: Any
    previous_customer_manager_link: Any
    new_manager: Any
    validate_only: Any

class CustomerManagerLinkOperation(proto.Message):
    update_mask: Any
    update: Any

class MutateCustomerManagerLinkResponse(proto.Message):
    results: Any

class MoveManagerLinkResponse(proto.Message):
    resource_name: Any

class MutateCustomerManagerLinkResult(proto.Message):
    resource_name: Any
