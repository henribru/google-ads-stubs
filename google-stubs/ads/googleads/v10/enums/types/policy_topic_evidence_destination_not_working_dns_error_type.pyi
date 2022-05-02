import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class PolicyTopicEvidenceDestinationNotWorkingDnsErrorTypeEnum(proto.Message):
    class PolicyTopicEvidenceDestinationNotWorkingDnsErrorType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        HOSTNAME_NOT_FOUND: int
        GOOGLE_CRAWLER_DNS_ISSUE: int
