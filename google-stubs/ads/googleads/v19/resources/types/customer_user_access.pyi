import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import access_role as gage_access_role

__protobuf__: Incomplete

class CustomerUserAccess(proto.Message):
    resource_name: str
    user_id: int
    email_address: str
    access_role: gage_access_role.AccessRoleEnum.AccessRole
    access_creation_date_time: str
    inviter_user_email_address: str
