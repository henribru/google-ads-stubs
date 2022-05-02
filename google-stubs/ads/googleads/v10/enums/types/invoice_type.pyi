import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class InvoiceTypeEnum(proto.Message):
    class InvoiceType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CREDIT_MEMO: int
        INVOICE: int
