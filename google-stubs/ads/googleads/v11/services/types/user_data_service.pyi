import proto
from _typeshed import Incomplete

from google.ads.googleads.v11.common.types import offline_user_data as offline_user_data

__protobuf__: Incomplete

class UploadUserDataRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    customer_match_user_list_metadata: Incomplete

class UserDataOperation(proto.Message):
    create: Incomplete
    remove: Incomplete

class UploadUserDataResponse(proto.Message):
    upload_date_time: Incomplete
    received_operations_count: Incomplete
