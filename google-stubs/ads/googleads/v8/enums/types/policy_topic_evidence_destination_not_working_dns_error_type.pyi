from typing import Any

import proto

__protobuf__: Any

class PolicyTopicEvidenceDestinationNotWorkingDnsErrorTypeEnum(proto.Message):
    class PolicyTopicEvidenceDestinationNotWorkingDnsErrorType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        HOSTNAME_NOT_FOUND: int
        GOOGLE_CRAWLER_DNS_ISSUE: int
