from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v15.enums.types.shared_set_status import SharedSetStatusEnum
from google.ads.googleads.v15.enums.types.shared_set_type import SharedSetTypeEnum

_M = TypeVar("_M")

class SharedSet(proto.Message):
    resource_name: str
    id: int
    type_: SharedSetTypeEnum.SharedSetType
    name: str
    status: SharedSetStatusEnum.SharedSetStatus
    member_count: int
    reference_count: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        type_: SharedSetTypeEnum.SharedSetType = ...,
        name: str = ...,
        status: SharedSetStatusEnum.SharedSetStatus = ...,
        member_count: int = ...,
        reference_count: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "id",
            "type_",
            "name",
            "status",
            "member_count",
            "reference_count",
        ],
    ) -> bool: ...
