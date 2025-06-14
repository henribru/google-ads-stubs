import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.common.types import offline_user_data
from typing import MutableSequence

__protobuf__: Incomplete

class UploadUserDataRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['UserDataOperation']
    customer_match_user_list_metadata: offline_user_data.CustomerMatchUserListMetadata

class UserDataOperation(proto.Message):
    create: offline_user_data.UserData
    remove: offline_user_data.UserData

class UploadUserDataResponse(proto.Message):
    upload_date_time: str
    received_operations_count: int
