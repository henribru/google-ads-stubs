from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class UserListCrmDataSourceTypeEnum(proto.Message):
    class UserListCrmDataSourceType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        FIRST_PARTY = 2
        THIRD_PARTY_CREDIT_BUREAU = 3
        THIRD_PARTY_VOTER_FILE = 4
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
