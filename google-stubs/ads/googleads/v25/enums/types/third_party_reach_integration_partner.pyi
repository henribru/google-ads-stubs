from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class ThirdPartyReachIntegrationPartnerEnum(proto.Message):
    class ThirdPartyReachIntegrationPartner(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NIELSEN = 2
        COMSCORE = 3
        KANTAR_MILLWARD_BROWN = 4
        VIDEO_RESEARCH = 5
        GEMIUS = 6
        MEDIA_SCOPE = 7
        AUDIENCE_PROJECT = 8
        VIDEO_AMP = 9
        ISPOT_TV = 10

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
