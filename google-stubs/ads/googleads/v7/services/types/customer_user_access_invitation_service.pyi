from typing import Any

import proto

from google.ads.googleads.v7.resources.types import (
    customer_user_access_invitation as customer_user_access_invitation,
)

__protobuf__: Any

class GetCustomerUserAccessInvitationRequest(proto.Message):
    resource_name: Any

class MutateCustomerUserAccessInvitationRequest(proto.Message):
    customer_id: Any
    operation: Any

class CustomerUserAccessInvitationOperation(proto.Message):
    create: Any
    remove: Any

class MutateCustomerUserAccessInvitationResponse(proto.Message):
    result: Any

class MutateCustomerUserAccessInvitationResult(proto.Message):
    resource_name: Any
