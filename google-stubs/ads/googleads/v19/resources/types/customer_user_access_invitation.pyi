import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import access_invitation_status, access_role as gage_access_role

__protobuf__: Incomplete

class CustomerUserAccessInvitation(proto.Message):
    resource_name: str
    invitation_id: int
    access_role: gage_access_role.AccessRoleEnum.AccessRole
    email_address: str
    creation_date_time: str
    invitation_status: access_invitation_status.AccessInvitationStatusEnum.AccessInvitationStatus
