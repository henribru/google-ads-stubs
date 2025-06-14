import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import custom_audience_member_type, custom_audience_status, custom_audience_type
from typing import MutableSequence

__protobuf__: Incomplete

class CustomAudience(proto.Message):
    resource_name: str
    id: int
    status: custom_audience_status.CustomAudienceStatusEnum.CustomAudienceStatus
    name: str
    type_: custom_audience_type.CustomAudienceTypeEnum.CustomAudienceType
    description: str
    members: MutableSequence['CustomAudienceMember']

class CustomAudienceMember(proto.Message):
    member_type: custom_audience_member_type.CustomAudienceMemberTypeEnum.CustomAudienceMemberType
    keyword: str
    url: str
    place_category: int
    app: str
