import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import shared_set_status, shared_set_type

__protobuf__: Incomplete

class SharedSet(proto.Message):
    resource_name: str
    id: int
    type_: shared_set_type.SharedSetTypeEnum.SharedSetType
    name: str
    status: shared_set_status.SharedSetStatusEnum.SharedSetStatus
    member_count: int
    reference_count: int
