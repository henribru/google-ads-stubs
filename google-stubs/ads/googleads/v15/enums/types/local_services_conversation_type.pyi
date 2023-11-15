from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class LocalServicesLeadConversationTypeEnum(proto.Message):
    class ConversationType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        EMAIL = 2
        MESSAGE = 3
        PHONE_CALL = 4
        SMS = 5
        BOOKING = 6
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
