from typing import Any

import proto

class PolicyTopicEvidenceDestinationNotWorkingDnsErrorTypeEnum(proto.Message):
    class PolicyTopicEvidenceDestinationNotWorkingDnsErrorType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        HOSTNAME_NOT_FOUND = 2
        GOOGLE_CRAWLER_DNS_ISSUE = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
