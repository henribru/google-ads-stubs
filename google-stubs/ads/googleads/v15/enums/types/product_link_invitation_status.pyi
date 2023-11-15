from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class ProductLinkInvitationStatusEnum(proto.Message):
    class ProductLinkInvitationStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ACCEPTED = 2
        REQUESTED = 3
        PENDING_APPROVAL = 4
        REVOKED = 5
        REJECTED = 6
        EXPIRED = 7
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
