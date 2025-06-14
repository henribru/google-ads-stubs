import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class LocalServicesLeadConversationTypeEnum(proto.Message):
    class ConversationType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        EMAIL: int
        MESSAGE: int
        PHONE_CALL: int
        SMS: int
        BOOKING: int
        WHATSAPP: int
        ADS_API: int
