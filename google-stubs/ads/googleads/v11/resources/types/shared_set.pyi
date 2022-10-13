from typing import Any

import proto

from google.ads.googleads.v11.enums.types.shared_set_status import SharedSetStatusEnum
from google.ads.googleads.v11.enums.types.shared_set_type import SharedSetTypeEnum

class SharedSet(proto.Message):
    resource_name: str
    id: int
    type_: SharedSetTypeEnum.SharedSetType
    name: str
    status: SharedSetStatusEnum.SharedSetStatus
    member_count: int
    reference_count: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        type_: SharedSetTypeEnum.SharedSetType = ...,
        name: str = ...,
        status: SharedSetStatusEnum.SharedSetStatus = ...,
        member_count: int = ...,
        reference_count: int = ...
    ) -> None: ...
