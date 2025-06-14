import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.resources.types import customer_user_access_invitation

__protobuf__: Incomplete

class MutateCustomerUserAccessInvitationRequest(proto.Message):
    customer_id: str
    operation: CustomerUserAccessInvitationOperation

class CustomerUserAccessInvitationOperation(proto.Message):
    create: customer_user_access_invitation.CustomerUserAccessInvitation
    remove: str

class MutateCustomerUserAccessInvitationResponse(proto.Message):
    result: MutateCustomerUserAccessInvitationResult

class MutateCustomerUserAccessInvitationResult(proto.Message):
    resource_name: str
