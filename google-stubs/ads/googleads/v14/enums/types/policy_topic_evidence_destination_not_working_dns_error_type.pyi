from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class PolicyTopicEvidenceDestinationNotWorkingDnsErrorTypeEnum(proto.Message):
    class PolicyTopicEvidenceDestinationNotWorkingDnsErrorType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        HOSTNAME_NOT_FOUND = 2
        GOOGLE_CRAWLER_DNS_ISSUE = 3
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
