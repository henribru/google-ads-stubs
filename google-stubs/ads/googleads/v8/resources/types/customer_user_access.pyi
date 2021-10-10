from typing import Any

import proto

__protobuf__: Any

class CustomerUserAccess(proto.Message):
    resource_name: Any
    user_id: Any
    email_address: Any
    access_role: Any
    access_creation_date_time: Any
    inviter_user_email_address: Any
