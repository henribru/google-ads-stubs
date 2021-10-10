from typing import Any

import proto

from google.ads.googleads.v8.common.types import offline_user_data as offline_user_data

__protobuf__: Any

class UploadUserDataRequest(proto.Message):
    customer_id: Any
    operations: Any
    customer_match_user_list_metadata: Any

class UserDataOperation(proto.Message):
    create: Any
    remove: Any

class UploadUserDataResponse(proto.Message):
    upload_date_time: Any
    received_operations_count: Any
