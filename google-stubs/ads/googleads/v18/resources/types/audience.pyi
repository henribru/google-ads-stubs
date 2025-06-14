import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.common.types import audiences
from google.ads.googleads.v18.enums.types import audience_scope, audience_status
from typing import MutableSequence

__protobuf__: Incomplete

class Audience(proto.Message):
    resource_name: str
    id: int
    status: audience_status.AudienceStatusEnum.AudienceStatus
    name: str
    description: str
    dimensions: MutableSequence[audiences.AudienceDimension]
    exclusion_dimension: audiences.AudienceExclusionDimension
    scope: audience_scope.AudienceScopeEnum.AudienceScope
    asset_group: str
