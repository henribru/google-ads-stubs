from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class CampaignDraftStatusEnum(proto.Message):
    class CampaignDraftStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        PROPOSED = 2
        REMOVED = 3
        PROMOTING = 5
        PROMOTED = 4
        PROMOTE_FAILED = 6
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
