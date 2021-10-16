from typing import Any

import proto

from google.ads.googleads.v8.enums.types import (
    access_invitation_status as access_invitation_status,
)

__protobuf__: Any

class CustomerUserAccessInvitation(proto.Message):
    resource_name: Any
    invitation_id: Any
    access_role: Any
    email_address: Any
    creation_date_time: Any
    invitation_status: Any
