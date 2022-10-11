import proto
from _typeshed import Incomplete

from google.ads.googleads.v11.resources.types import (
    customer_user_access_invitation as customer_user_access_invitation,
)

__protobuf__: Incomplete

class MutateCustomerUserAccessInvitationRequest(proto.Message):
    customer_id: Incomplete
    operation: Incomplete

class CustomerUserAccessInvitationOperation(proto.Message):
    create: Incomplete
    remove: Incomplete

class MutateCustomerUserAccessInvitationResponse(proto.Message):
    result: Incomplete

class MutateCustomerUserAccessInvitationResult(proto.Message):
    resource_name: Incomplete
